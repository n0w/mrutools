# - mrutools - A python tool for managing linux MRU files
# - DragonPlayer Plugin
# - tab spacing: 4
from os import listdir,environ
from os.path import isfile, join, getatime, getmtime
import time, datetime
import re
import dateutil.parser

from MRUModules import mruOBJ
        
class DragonPlayerPlugin:
    def __init__(self, incomingDict):
        # incomingDict var is list object coming from main module.
        # here we extract and append MRUs from KDE
        self.MRUList = []
        self.MRUPath = environ['HOME']+"/.kde/share/config/dragonplayerrc"

        print "running...",

        self.getMRUList()
        incomingDict['dragonplayer'] = self.MRUList

        print "[OK: retrieved %d elements]" % len(self.MRUList)

    def getMRUList(self):
        
        f = open(self.MRUPath)
        insideMRU = False

        # Extract info from within the file
        for line in f:
            # Clear trailing whitespaces
            line = line.rstrip()
            if line[0:6] == "[file:":
                # line var contains MRU name now. In order to be able to
                # extract the date later, we set insideMRU flag True.
                tempMRU = mruOBJ.mruClass()
                insideMRU = True
                
                # Name will be within brackets: [file:///....]
                # We use a regex to extract the URL
                tempMRU.URL = re.match(r"\[([^]]*)\]", line).groups()[0]
                
            if line[0:4] == "Date" and insideMRU == True:
                tempMRU.accessDate = dateutil.parser.parse(line.split("=")[1])
                tempMRU.lastApp = "dragonplayer"
                self.MRUList.append(tempMRU)
                insideMRU = False

        f.close()
                    
            
def run(incomingList):
    myDragonPlayer = DragonPlayerPlugin(incomingList)
