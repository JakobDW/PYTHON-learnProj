#Different tests

import re

def fun(tex,con):
    check = re.compile(con) #look for grups of small letters

    result = check.findall(tex)

    print(result)


text ='Suchą szosą69 szła Sasza'

cond = '\w\w\w\d'

fun(text,'\w\w\w\d')