#textFilesOverview.py - find user defined str 
#                       in lines of
#                       all text files
#                       in user defined directory
                        
################################################################################################################################################################

import re, os

print('Current working directory:')                                                                             #Print cwd
print(os.getcwd())
print()
################################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Loop to decide cwd



while(True):                                                                                                    #Ask if cwd is ok or change to user defined cwd

    print('Provide new cwd(if no, press enter):')

    cwd=''

    cwd = input()

    if cwd != '':                                                                                               #If user defined new cwd

        ex = os.path.exists(cwd)                                                                                #Check if path exists

        dir = os.path.isdir(cwd)                                                                                #Check if path lead to directory

        if ex == True and dir == True:                                                                          #If both is true change cwd
            os.chdir(cwd)
            print()
            print('Current working directory:')
            print(os.getcwd())
            print()

            break

        else:
            print('Incorrect cwd path')
            print()
    else:                                                                                                       #If cwd not to be changed break
        print()
        break

#End loop to decide cwd
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################################################
print('Current working directory:')
print(os.getcwd())
print()

fileList = os.listdir(os.getcwd())                                                                              #get list of files from cwd
################################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Separate text files from fileList

txtFileList = []

regEx = re.compile('\.txt')

for file in range(len(fileList)):                                                                                #For every file on file list

    res = regEx.search(fileList[file])                                                                           #Search for .txt extension

    if res != None:                                                                                              #If .txt extension is present in searched file name
        txtFileList.append(fileList[file])

#End text file selection 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################################################
if not txtFileList:
    print('There are no text files in cwd')
    print()
################################################################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Define regEx you want to look for in those files and 
else:
    print('Define regular expression to look for(remember of \'\')')                                             #As described
    reg = input()

    regEx = re.compile(reg)

    discMachLines={}

    for file in txtFileList:                                                                                     #For every file on txtFileList
        openFile = open(file,'r')                                                                                #Open to read
        fileInLines = openFile.readlines()                                                                       #Save to list in lines
        openFile.close()                                                                                         #Close
        for line in fileInLines:                                                                                 #For every line in fileInLines
            res = regEx.search(line)                                                                             #Search for maching regular expression
            if res != None:                                                                                      #If found mach
                if file in discMachLines:
                    discMachLines[file] += line
                else:
                    discMachLines[file] = line                                                                   #Save line under according key in dictionary

#End of searchng through text files lines
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################################################

      
print (discMachLines)

