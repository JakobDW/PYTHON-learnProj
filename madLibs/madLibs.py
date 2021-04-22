#madLibs.py - imitation of cards against humanity game

import re

def swaper(key_list,ansDict,sentence):
    for i in range(len(key_list)):

       spl = sentence.split(keyList[i])

       newSen = spl[0] + ansDict[i] + spl[1]

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





#TODO print the results