import argparse
import imp
import os
import colored_traceback
import sys
from MRUModules import PDFExport
import MRUModules
import time
import platform

# TODO: Use colorama to eye-candify output
#       https://pypi.python.org/pypi/colorama
#
# TODO: Unify date representation format -DONE
# TODO: Timeline
# TODO: Rethink MRU list implementation; JSON? We need to know which plugin stores what. - DONE
# TODO: Specify if live system or disk image/whatever via command-line
# TODO: Consider if having name and url attributes is really necessary

#VLC Plugin:
    #n0w@n0wDesk:~$ cat .config/vlc/vlc-qt-interface.conf 
    #[General]
    #IsFirstRun=0
    #geometry=@ByteArray(\x1\xd9\xd0\xcb\0\x1\0\0\0\0\x2(\0\0\0\xaa\0\0\x6\x1a\0\0\x3.\0\0\x2/\0\0\0\xc8\0\0\x6\x13\0\0\x3'\0\0\0\0\0\0)
    #filedialog-path=/home/n0w

    #[RecentsMRL]
    #list=file:///media/denna/dl/seeding/Peliculas/Crash%20(2004)/Crash.2004.720p.BluRay.x264.YIFY.mp4, file:///media/denna/dl/seeding/Peliculas/Blue%20Jasmine%20(2013)/Blue.Jasmine.2013.720p.BluRay.x264.YIFY.mp4

# tons of interesting files: n0w@nLap:~/.kde/share/config$ 

# Dragon Player
# Mucha mas informacion de la que muestra. No borra ;)
# n0w@n0wDesk:~/.kde/share/config$ cat dragonplayerrc

__VERSION__ = "0.3"
__AUTHOR__ = "           Angel Suarez-B (n0w)"
__DATE__ = "19/03/2015"

class MRUTools:
    def __init__(self,outputMode):
        # Plugin & Init Stuff
        # ===================
        self.PluginFolder = "./plugins"
        self.MainModule = "__init__"
        self.outputMode = outputMode
        self.showBanner()
        self.plugins = []
        self.loadedPlugins = []
        
        # Set hook to colored_traceback
        colored_traceback.add_hook()

        if self.outputMode == "usage":
            print "Usage: ./mrutools.py --[stdout,file]"
            exit(-1)

        # MRU Stuff
        # =========
        # MRUDict: Key is plugin name
        #
        self.MRUDict = {}

        # Contains hardware, mem, proc, etc. info
        self.systemInfo = []

        # Go go go!
        self.go()
      
    def getSystemInfo(self):
        print "[+] Gathering system information...",   
        kernelInfo = ""
        for element in platform.uname(): 
            kernelInfo = kernelInfo + " " + element 

        self.systemInfo.append(kernelInfo)
        print "[OK]"

    def go(self):

        self.getSystemInfo()
        
        self.getPlugins()
        print "[+] Found %d plugin(s)!" % len(self.plugins)
        
        for plugin in self.plugins:
            print " |---> "+ plugin["name"] + "...",
            loadedPlugin = self.loadPlugin(plugin)
            loadedPlugin.run(self.MRUDict)
            self.loadedPlugins.append(loadedPlugin)

        if self.outputMode == "pdf":
            fileName = "MRUtools report %s" % time.ctime()
            print " |"
            print "[+] Writing to disk: %s" % fileName
            
            myRep = PDFExport.Reporter(self.MRUDict, fileName)
            
        if self.outputMode == "stdout":
            print " |"
            print "[+] Writing report to stdout:\n"
        
            print "+---------------------------+"
            print "| MRUTools Forensics Report |"
            print "+---------------------------+"
            print "\n * Generated on " + time.ctime() + "\n"
            print " * System Information:"
            
            print "    > Kernel:" +  self.systemInfo[0]
            print "    > Mem:"            
            print "    > CPU:"
            print "    > PCI:"
            print "    > USB:"
            print "\n * Recovered MRU Data:\n"
            
            for pluginName,pluginResult in self.MRUDict.iteritems():
                print "[>]" + pluginName
                print "-" * (len(pluginName) + 3)
                for element in pluginResult:
                    element.show()
        
    def showBanner(self):
        print "MRUTools - v" + __VERSION__
        print __AUTHOR__ + " \n"
        
        
    def getPlugins(self):
        dirList = os.listdir(self.PluginFolder)
        
        for i in dirList:
            location = os.path.join(self.PluginFolder, i)
            if not os.path.isdir(location) or \
               not self.MainModule + ".py" in os.listdir(location):
                continue

            info = imp.find_module(self.MainModule, [location])
            self.plugins.append({"name": i, "info": info})

    def loadPlugin(self,plugin):
        return imp.load_module(self.MainModule, *plugin["info"])


if __name__ == "__main__":
    # Get output to screen or file... or who knows? :D
    # TODO: This is quick'n'dirty: Use argparse instead!!
    if len(sys.argv) > 1:
        if (sys.argv[1] == "--stdout"):
            myMRU = MRUTools("stdout")
            exit(0)
            
        elif (sys.argv[1] == "--pdf"):
            myMRU = MRUTools("pdf")
            exit(0)

    myMRU = MRUTools("usage")
    