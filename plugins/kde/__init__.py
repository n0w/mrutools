# - mrutools - A python tool for managing linux MRU files
# - KDE Plugin
# - tab spacing: 4
from os import listdir,environ
from os.path import isfile, join, getatime, getmtime
import time, datetime
from MRUModules import mruOBJ
        
class KDEPlugin:
    def __init__(self, incomingDict):
        # incomingDict var is list object coming from main module.
        # here we extract and append MRUs from KDE
        self.MRUList = []
        self.MRUPath = environ['HOME']+"/.kde/share/apps/RecentDocuments/"

        print "running...",

        self.getMRUList()
        incomingDict['kde'] = self.MRUList

        print "[OK: retrieved %d elements]" % len(self.MRUList)

    def getMRUList(self):
        fileList = [ f for f in listdir(self.MRUPath) if isfile(join(self.MRUPath,f)) ]
        

        for foundFile in fileList:
            try:
                f = open(self.MRUPath+foundFile)
                # Extract info from within the file
                for line in f:
                    # Clear trailing whitespaces
                    line = line.rstrip()
                    if line[0:4] == "Name":
                        tempMRU.name = line.split("=")[1]
                    if line[0:3] == "URL":
                        tempMRU.URL = line.split("=")[1]
                    if line[0:20] == "X-KDE-LastOpenedWith":
                        tempMRU.lastApp = line.split("=")[1]
    
                f.close()
                
                # Extract date info from OS (epoch)
                # then convert them to datetime objects
                epochTime = getatime(self.MRUPath+foundFile)
                tempMRU.accessDate = datetime.datetime.fromtimestamp(epochTime)
                
                epochTime = getmtime(self.MRUPath+foundFile)
                tempMRU.modifyDate = datetime.datetime.fromtimestamp(epochTime)
                
                # Append new element to internal list
                self.MRUList.append(tempMRU)

            except Exception,e:
                print "\n |(!)-> {}".format(e)
            tempMRU = mruOBJ.mruClass()


            
            # DEBUG - Show it!
            # tempMRU.DEBUG_Show()
            
def run(incomingList):
    myKDE = KDEPlugin(incomingList)
