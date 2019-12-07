#!/usr/bin/env python3

#############################################
# Author: Jorin Grant                       #
#############################################

import PyPDF2
import os
import sys
import subprocess
from PyPDF2 import PdfFileWriter, PdfFileReader

import colored
from colorama import Fore, Back, Style

'''	View if PDF has JavaScript in it
pdfinfo sample_JavaScript.pdf | grep JavaScript | cut -d ":" -f2 | cut -d " " -f6


	View JavaScript inside of file
pdfinfo -js sample_JavaScript.pdf'''

class pdfDocuments:
    def __init__(self):
        #self.allPDFDocuments = allPDFDocuments
        self.allPDFDocuments = sys.argv[1:]

    # create a copy of the PDF file with out any text
    def redactPDF(self, allPDFDocuments):
        for uniqueDocument in allPDFDocuments:
            try:
                print(f"Redacting: {uniqueDocument}")
                newDocumentName = uniqueDocument.strip(".pdf") + "_REDACTED.pdf" # create new name
                originalPDF = PdfFileReader(open(uniqueDocument, "rb"),strict=False)
                redactedPDF = PdfFileWriter()

                [redactedPDF.addPage(originalPDF.getPage(i)) for i in range(originalPDF.getNumPages())] #add all the pages from the original document to the new to-be-redacted document
                redactedPDF.removeText() #remove text from the next document

                redactedPDF.write(open(newDocumentName, "wb")) # write new document
            except Exception as e:
                e = str(e)
                print(f'\t{e}\n')
                pass
                

if __name__ == "__main__":
    pdfDocuments().redactPDF(sys.argv[1:]) # for redactPDF class
