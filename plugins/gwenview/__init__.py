# - mrutools - A python tool for managing linux MRU files
# - KDE Plugin
# - tab spacing: 4
from os import listdir,environ
from os.path import isfile, join, getatime, getmtime
from MRUModules import mruOBJ
import time
import dateutil.parser
       
class GwenviewPlugin:
    def __init__(self, incomingDict):
        # incomingDict var is dictionary object coming from main module.
        # here we extract and append MRUs from KDE
        self.MRUList = []
        self.MRUPath = environ['HOME']+"/.kde/share/apps/gwenview/recentfolders/"

        print "running...",

        self.getMRUList()
        incomingDict['gwenview'] = self.MRUList

        print "[OK: retrieved %d elements]" % len(self.MRUList)

    def getMRUList(self):
        fileList = [ f for f in listdir(self.MRUPath) if isfile(join(self.MRUPath,f)) ]
        
        for foundFile in fileList:
            try:
                f = open(self.MRUPath+foundFile)
                tempMRU = mruOBJ.mruClass()                

                # Extract info from within the file
                for line in f:
                    # Clear trailing whitespaces
                    line = line.rstrip()
                    if line[0:8] == "dateTime":
                        tempMRU.accessDate = dateutil.parser.parse(line.split("=")[1])
                    if line[0:3] == "url":
                        tempMRU.URL = line.split("=")[1]
                
                f.close()
                tempMRU.lastApp = "gwenview"
            except:
                pass
            # Append new element to internal list
            self.MRUList.append(tempMRU)

            # DEBUG - Show it!
            # tempMRU.DEBUG_Show()
            
def run(incomingList):
    myGwenview = GwenviewPlugin(incomingList)

