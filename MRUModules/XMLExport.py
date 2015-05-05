'''
Created on Apr 29, 2015

@author: n0w
'''
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom
from datetime import datetime


class XMLExporter:
    def __init__(self, MRUDict, fileName):
        # Root element
        self.timeline = None
        
        # Add timeline "metadata"
        self.buildSkeleton()
        
        # Each timeline category corresponds to a MRUTools plugin
        self.addCategories(MRUDict)
        
        # Add MRU Data
        self.addEvents(MRUDict)
        
        # Make output a little prettier by adding spaces and indentation
        output = self.prettify()
        
        # Write file to disk
        f = open(fileName, 'w')
        f.write(output.encode('utf8'))
        f.close()
        
        print "[OK]"
        
        pass
    
    def prettify(self):
        rough_string = ElementTree.tostring(self.timeline, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="   ")
    
    def addCategories(self, MRUDict):
        categories = SubElement(self.timeline, "categories")
        
        for pluginName,pluginResult in MRUDict.iteritems():         
            newCat = SubElement(categories, "category")
            SubElement(newCat, "name").text = pluginName
            SubElement(newCat, "color").text = "255,255,255"
            SubElement(newCat, "progress_color").text = "255,255,255"
            SubElement(newCat, "done_color").text = "255,255,255"
            SubElement(newCat, "font_color").text = "0,0,0"
    
    def buildSkeleton(self):
        self.timeline = Element("timeline")
        SubElement(self.timeline, "version").text = "1.5.0"
        SubElement(self.timeline, "timetype").text = "gregoriantime"
    
    
    def addEvents(self, MRUDict):
        events = SubElement(self.timeline, "events")

        # Find max and min date values to set initial Timeline view in order to
        # be able to visualize every MRU file.
        minDate = None
        maxDate = None
        
        for pluginName,pluginResult in MRUDict.iteritems():  
            for element in pluginResult:
                
                # Date threshold initialization
                if minDate == None:
                    minDate = element.accessDate                
                if maxDate == None:
                    maxDate = element.accessDate

                # Date threshold check
                if minDate > element.accessDate:
                    minDate = element.accessDate
                
                if maxDate < element.accessDate:
                    maxDate = element.accessDate

                # Some elements may contain fractions of a second.
                # Timeline does not support that so we have to discard that info.
                trimmedDate = element.accessDate.strftime("%Y-%m-%d %H:%M:%S")
                
                newEvent = SubElement(events, "event")
                SubElement(newEvent, "start").text = str(trimmedDate)
                SubElement(newEvent, "end").text = str(trimmedDate)
                SubElement(newEvent, "text").text = unicode(element.URL, "utf-8")
                SubElement(newEvent, "progress").text = "100"
                SubElement(newEvent, "fuzzy").text = "False"   
                SubElement(newEvent, "locked").text = "False"
                SubElement(newEvent, "ends_today").text = "False"
                SubElement(newEvent, "category").text = pluginName
                
                if element.lastApp != "":   
                    SubElement(newEvent, "description").text =  "Last opened with: " + element.lastApp
                else:
                    SubElement(newEvent, "description").text = "No data available."
            
        newView = SubElement(self.timeline, "view")
        displayedPeriod = SubElement(newView, "displayed_period")    
        SubElement(displayedPeriod, "start").text = str(minDate.strftime("%Y-%m-%d %H:%M:%S"))
        SubElement(displayedPeriod, "end").text = str(maxDate.strftime("%Y-%m-%d %H:%M:%S"))
        
        SubElement(newView, "hidden_categories")
            
            
            
            
            