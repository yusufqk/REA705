#!/usr/bin/python3

#specific to extracting information from word documents
import os
import sys
import zipfile#other tools useful in extracting the information from our document
import re#to pretty print our xml:
import xml.dom.minidom
from terminaltables import AsciiTable
from modules.post_create import create_file
from modules.post_url import create_url
from modules.post_many import multiple
from regex import findText


class WordDoc:

    def __init__(self):

        self.text = "document.xml"

        self.document = zipfile.ZipFile(sys.argv[1])

        self.table = [["Object", "Path"]]


    def results(self, xmlfiles):

        #print(xmlfiles)

        for i in range(len(xmlfiles)):

            file_break = xmlfiles[i].split(".")

            if "xls" in file_break:

                self.table.append(["Excel",xmlfiles[i]])

            if "bin" in file_break:

                self.table.append(["VBA",xmlfiles[i]])


    def ddefind(self):

        with open("word/document.xml","r") as fobj:
            everything = fobj.read()

        result = everything.find("DDEAUTO")

        if result != -1:

            everything = list(everything)

            ddestring = ""
            for i in range(result,len(everything)):

                if everything[i] == "<":
                    break
                else:
                    ddestring += everything[i]

            #print(ddestring)

            self.table.append(["DDE",ddestring])

            with open("document.xml","r") as fobj:
                newstring = fobj.read()


            ddestring = " </w:rPr><w:instrText>" + ddestring + "<w:instrText></w:r> "

            newstring = list(newstring)
            newstring[2430] = ddestring
            newstring = "".join(newstring)

            with open("document.xml","w") as fobj:
                fobj.write(newstring)

    def main(self):


        #print(self.document.namelist())

        #print(type(document))

        #self.document.extractall()

        #check for dde

        self.ddefind()

        findText()

        #os.system("cp word/document.xml study.xml")
        #os.system("rm word/document.xml")
        #os.system("cp document.xml word/document.xml")

        with zipfile.ZipFile("newdoc.doc", "w") as docx:
                    for filename in self.document.namelist():
                        #if filename == "word/document.xml":
                            #filename == "yu.xml"
                            #docx.write(filename)
                            #continue
                        #else:
                        #print(filename)
                        docx.write(filename)


        xmlfiles = self.document.namelist()

        #os.system("rm _rels/ docProps/ '[Content_Types].xml' -fr")

        self.results(xmlfiles)

        self.table = AsciiTable(self.table)

        print("[*] File successfully redacted: newdoc.docx")
        print(self.table.table)

        newfiles = zipfile.ZipFile("newdoc.doc")

        #print(newfiles.namelist())

        #create_file()

        #multiple()

test = WordDoc()
test.main()
