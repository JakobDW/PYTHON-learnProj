#textFilesOverview.py - find user defined str 
#                       in lines of
#                       all text files
#                       in user defined directory
                        
#***************************************************************************************************************************************************

import re, os

print('Current working directory:')                                                                             #Print cwd
print(os.getcwd())
print()

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
        break

#End loop to decide cwd
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

print(os.getcwd())

fileList = os.listdir(os.getcwd())

print(fileList)
