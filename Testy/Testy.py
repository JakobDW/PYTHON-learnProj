#Different tests

import re

def fun(tex,con):
    check = re.compile('[a-z]') #look for grups of small letters

    result = check.search(tex)

    print(result)



text ='Suchą szosą69 szła Sasza'

cnd =r'(a-z)+'

fun(text, cnd)

    checkList = {len:       [False,'Password must be 8 at least letters long'],
                 smallL:    [False,'Use also small letters'],
                 bigL:      [False,'Use also big letters'],
                 num:       [False,'Use also numbers'],
                 specSig:   [False,'Use also special signs']}
