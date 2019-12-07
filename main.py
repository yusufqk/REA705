#!/usr/bin/env python3
import sys # take CLI input as files to be redacted
import io  # for determining file type (BytesIO)

#from pdfredaction import redactPDF # Jorin's code
from parsedoc import WordDoc   # Yusuf's code

# This main function will loop through all CLI listed documents and determine its file type by looking at the header
# From there it will send the file to the appropriate class to be redacted
def main(allDocuments):
    for uniqueDocument in allDocuments: # look at each document to determine it's file type
        with open(uniqueDocument, 'rb') as file:
            fileHeader = file.read(1024)
            pdfBytes  = "%PDF".encode()
            docBytes  = bytes.fromhex("d0cf 11e0 a1b1 1ae1") # .doc files have no ASCII for its signature so we use the hex equivalent instead
            docxBytes = "PK".encode()
            if pdfBytes in fileHeader:
                print(f'{uniqueDocument} is a PDF file')
                redactPDF(uniqueDocument)
            elif docBytes or docxBytes in fileHeader:
                print(f'{uniqueDocument} is a .doc or .docx file')
                doc_submit = WordDoc(uniqueDocument)
                doc_submit.main()

            else:
                print(f'\tCould not determine file type for {uniqueDocument}')
                print('\t',docBytes)
                print('\t',fileHeader[:50])






if __name__ == '__main__':
    main(sys.argv[1:]) # send all CLI listed files to the main function to determine document type
