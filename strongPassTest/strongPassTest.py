#Test Force of Password
import re



def isIncluding(condition, text): #Get condition str to test and str to test
  
    regEx = re.compile(condition)

    res = regEx.search(text)

    if res == None:               #Function return False if condition str was not found in password str
        return  False
    else:
        return  True



def passwordTest(password):       #Call isIncluding for different conditions you want to test
    
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
        return True               #Return True if all conditions are True



haslo = 'AMISZed69!#'

if passwordTest(haslo) == True:
  print('Hasło POTĘŻNE!')
else:
    print('Hasło słabiutkie...')



