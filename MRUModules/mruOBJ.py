import time

class mruClass:
    '''
    Class for managing MRU data
    '''

    def __init__(self):
        self.name = ""
        self.accessDate = "" # both datetime objects!
        self.modifyDate = ""
        self.URL = ""
        self.lastApp = ""

    def show(self):
        if self.name != "":
            print " |  Name: " + self.name
        if self.accessDate != "":
            print " |  Last Access Date: " + str(self.accessDate)
        if self.modifyDate != "":
            print " |  Last Modification Date: " + str(self.modifyDate)
        if self.URL != "":
            print " |  URL: " + self.URL
        if self.lastApp != "":   
            print " |  Last opened with: " + self.lastApp
        print " |"
        
