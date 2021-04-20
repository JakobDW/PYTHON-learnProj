#Different tests

import re

def fun(tex,con):
    check = re.compile('[a-z]') #look for grups of small letters

    result = check.search(tex)

    print(result)



text ='Suchą szosą69 szła Sasza'

cnd =r'(a-z)+'

fun(text, cnd)

