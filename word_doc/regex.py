#!/usr/bin/python3
import re
import sys

# </w:t>
def findText():
    #documentFile      = 'study.xml' # XML file to perform regex on

    with open("word/document.xml","r") as fobj:
        lines = fobj.read().splitlines()

    string = lines[1]

    tagRegEx = '\<w:t\>[\w\s]+\<\\/w:t\>'
    displayedTextList = re.findall(tagRegEx, string) # use regex to find all instances of the tags (<w:t>.......</w:t>) & then add it to a list (displayedTextList)

    if len(displayedTextList) == 0:
        print("Look at me!")
        return

    locationOfTags = re.search(tagRegEx, string)
    print('-' * 80)
    print('\t\tProof that regex works')
    print('-' * 80)
    print(f'All found instances: {displayedTextList}')
    print(f'All locations: {locationOfTags.span()}') # only prints location of 1st object in list, not all
    print('\n\n')

    print('-' * 80)
    print('\t\tReplace regex match with a single string')
    print('-' * 80)
    x = re.sub('\<w:t\>[\w\s]+\<\\/w:t\>',"******************************************",string)
    print(x)
    print('\n\n')

    print('-' * 80)
    print('\t\tLocation and string content for each match')
    print('-' * 80)
    for m in re.finditer('\<w:t\>[\w\s]+\<\\/w:t\>',string):
        print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    print('\n\n')

    print('-' * 80)
    print('\t\tReplace each match with length of string')
    print('-' * 80)
    stringTwo = '</w:sectPr><w:r><w:t>Python Black and his magic</w:t></w:r></w:body></w:document>'
    newString = ''
    for i in range(len(displayedTextList)):
        print(displayedTextList[i]) # DEBUG:
        whitespaceLength = '<w:t>' + ' ' * (len(displayedTextList[i]) - 11) + '</w:t>'
        if i == 0:
            #newString = string.replace(displayedTextList[i], whitespaceLength) # only Python Black string replacement working for some reason
            newString = string.replace(displayedTextList[i], "")
        else:
            #newString = newString.replace(displayedTextList[i], whitespaceLength)
            newString = newString.replace(displayedTextList[i], "")
        # print(newString+ '\n')
    print(newString)
    print('\n\n')

    finalstring = lines[0] + "\n" + newString

    print(finalstring)

    with open("word/document.xml","w") as fobj:
        fobj.write(finalstring)




