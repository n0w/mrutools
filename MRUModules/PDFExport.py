'''
Created on Mar 22, 2015

@author: n0w
'''

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

import time

class Reporter:
    def __init__(self, MRUDict, systemInfo, fileName):
        self.PAGE_HEIGHT = defaultPageSize[1]
        self.PAGE_WIDTH = defaultPageSize[0]
        self.IMG_LOGO = "resources/logo.png"
        self.styles = getSampleStyleSheet()
        self.Title = "MRUTools Forensics Report"
        self.Subtitle = "Generated on " + time.ctime()
        self.go(MRUDict,systemInfo, fileName)
    
    def myFirstPage(self, canvas, doc):
        canvas.saveState()
        canvas.drawImage(self.IMG_LOGO, 30, self.PAGE_HEIGHT - 80, height=60, width=74, mask='auto')
        
        canvas.setFont('Times-Bold', 16)
        canvas.drawCentredString(self.PAGE_WIDTH / 2.0, self.PAGE_HEIGHT - 48, self.Title)
        canvas.setFont('Times-Bold', 14)
        canvas.drawCentredString(self.PAGE_WIDTH / 2.0, self.PAGE_HEIGHT - 66, self.Subtitle)
        canvas.setFont('Times-Roman', 9)
        canvas.drawString(inch, 0.75 * inch, "%s Page 1" % self.Title)
        canvas.restoreState()
        
    def myLaterPages(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 9)
        canvas.drawString(inch, 0.75 * inch, "%s Page %d" % (self.Title, doc.page))
        canvas.restoreState()
        
    def go(self, MRUDict, systemInfo, fileName):
        doc = SimpleDocTemplate(fileName)
        Story = [Spacer(1, 0.5 * inch)]
        style = self.styles["Normal"]
        pos = 1
        
        # Machine information
        header = "<strong>Machine Information</strong>" + "<br/>"
        p = Paragraph(header, style)
        Story.append(p)

        for element in systemInfo:         
            content = element + "<br/>"
            p = Paragraph(content,style)
            Story.append(p)

        Story.append(Spacer(1, 0.2 * inch))
        
        # Plugin information
        header = "<strong>Executive Summary</strong>" + "<br/>"
        p = Paragraph(header, style)
        Story.append(p)
        
        for pluginName,pluginResult in MRUDict.iteritems():         
            content = "   - " + pluginName + ": " + str(len(pluginResult)) + " extracted elements"+ "<br/>"
            p = Paragraph(content,style)
            Story.append(p)
            
        Story.append(Spacer(1, 0.2 * inch))
        
        # MRU Data
        header = "<strong>MRU Data</strong>" + "<br/><br/>"
        p = Paragraph(header, style)
        Story.append(p)
                     
        for pluginName,pluginResult in MRUDict.iteritems():         
            header = "<strong>" + str(pos) + ". " + pluginName + "</strong>"
            pos += 1
            p = Paragraph(header, style)
            Story.append(p)
           
            
            for element in pluginResult:
                content = "<strong>URL:</strong> " + element.URL  + "<br />"\
                        + "<strong>Last Access Date:</strong> " + str(element.accessDate) + "<br />"\
                        + "<strong>Last Application:</strong> " + element.lastApp
                p = Paragraph(content, style)
                Story.append(p)
                Story.append(Spacer(1, 0.2 * inch))

        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
    