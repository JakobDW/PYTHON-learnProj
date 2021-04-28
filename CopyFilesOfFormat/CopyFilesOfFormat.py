############################################################################################################################################################################
#Copy files of choosen format to desired folder(or new folder)
import os, shutil, re
from pathlib import Path
############################################################################################################################################################################
############################################################################################################################################################################
def getCwd():

    while(True):                                                                                                    #Ask if cwd is ok or change to user defined cwd,
                                                                                                                    #default cwd is file directory

        print('Provide directory to scan(for program file directory, press enter):')

        cwd=''

        cwd = input()

        if cwd != '':                                                                                               #If user defined new directory

            ex = os.path.exists(cwd)                                                                                #Check if path exists

            dir = os.path.isdir(cwd)                                                                                #Check if path lead to directory

            if ex == True and dir == True:                                                                          #If both is true change directory
                os.chdir(cwd)
                print()
                print('Current working directory:')
                print(os.getcwd())
                print()

                break

            else:
                print('Incorrect directory path')
                print()
        else:                                                                                                       #If cwd not to be changed break
            print()
            break

############################################################################################################################################################################
############################################################################################################################################################################

#TODO Define directory to walk thru ---
getCwd()

#TODO Define where to copy ---
print('Define path to backup directory')
print()
copyDirPath = input()

#TODO check if copyDirPath existts and is directory and if not, create it ---

if not os.path.exists(copyDirPath):
    os.makedirs(copyDirPath)


#TODO Define extension of files to copy
print('Define type of files to copy(ex: \.pdf)')
print()
extension = input()

#TODO create regEx ---

regEx = re.compile(extension)

#TODO  walk thru cwd and for every file name do regEx. If mach is  found copy this file to backup directory

top = os.getcwd()

for dirName, subDirs, fileNames in os.walk(os.getcwd()):
    for fileName in fileNames:
        os.chdir(dirName)
        mach = regEx.search(fileName)
        if mach != None:
            #shutil.copy(os.path.abspath(fileName),copyDirPath)
            shutil.copy(os.path.abspath(fileName),copyDirPath)
        os.chdir(top)
############################################################################################################################################################################
############################################################################################################################################################################