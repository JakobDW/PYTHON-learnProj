#Test Force of Password
import re



def isIncluding(condition, text):
  

 
    regEx = re.compile(condition)

    res = regEx.search(text)

    if res == None:
        return  False
    else:
        return  True



def passwordTest(password):
    
    if len(password)<8:
        return False
    if isIncluding('[a-z]',password) == False:
        return False
    if isIncluding('[A-Z]',password) == False:
        return False
    if isIncluding('[0-9]',password) == False:
        return False
    if isIncluding('[!@#$%^&*]',password) == False:
        return False
    else:
        return True



haslo = 'AMISZed69!#'

if passwordTest(haslo) == True:
  print('Hasło POTĘŻNE!')
else:
    print('Hasło słabiutkie...')



