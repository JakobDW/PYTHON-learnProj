#madLibs.py - imitation of cards against humanity game

import re

def swaper(keyList, ansDict, sentence):
    
    newSen =''

    for i in range(len(keyList)):

       
       spl = sentence.split(keyList[i])

       newSen = spl[0] + ansDict[keyList[i]] + spl[1]

    return newSen

sentenceFile = open('sentence.txt','r')

sentence = sentenceFile.read() 

sentenceFile.close()

print(sentence)

#TODO ask user to define swaps for NOUN, ADJECTIVE, VERB and ADVERB

words = {'NOUN':'','ADJECTIVE':'','VERB':'','ADVERB':''}

print('Provide noun:')
words['NOUN'] = input()

print('Provide adjective:')
words['ADJECTIVE'] = input()

print('Provide verb:')
words['VERB'] = input()

print('Provide adverb:')
words['ADVERB'] = input()


#TODO find those in text and swap them with user definitions


keysList = list(words.keys())


finalMess = swaper(keysList, words, sentence)

#TODO print the results

print()
print(finalMess)

