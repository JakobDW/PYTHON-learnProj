#! python3
#Different tests

import re, os

regEx = re.compile('\.txt')


for dirName, subDirs, fileNames in os.walk('.'):
    for fileName in fileNames:
        mach = regEx.search(fileName)
        if mach != None:
            print(os.path.abspath(fileName))


