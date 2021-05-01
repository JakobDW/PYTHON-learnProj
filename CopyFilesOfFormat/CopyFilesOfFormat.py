############################################################################################################################################################################
#Copy files of choosen format to desired folder(or new folder)
import os, shutil, re
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

#Define directory to walk thru 
getCwd()

#Define where to copy 
print('Define path to backup directory')
print()
copyDirPath = input()

#Check if copyDirPath exists and if not, create it

if not os.path.exists(copyDirPath):
    os.makedirs(copyDirPath)


#Define extension of files to copy
print('Define type of files to copy(ex: \.pdf)')
print()
extension = input()

#Create regEx 

regEx = re.compile(extension)

#Walk thru cwd and for every file name do regEx. If mach is  found copy this file to backup directory

top = os.getcwd()

for dirName, subDirs, fileNames in os.walk(os.getcwd()):
    for fileName in fileNames:
        os.chdir(dirName)
        mach = regEx.search(fileName)
        if mach != None:
            shutil.copy(os.path.abspath(fileName),copyDirPath)
        os.chdir(top)
############################################################################################################################################################################
############################################################################################################################################################################