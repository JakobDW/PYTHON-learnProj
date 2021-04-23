#madLibs.py - imitation of cards against humanity game

import re

def swaper(keyList, ansDict, sentence):                                    #swap templates with user answers
    
    newSen = sentence

    for i in range(len(keyList)):                                          #for every template

       
       spl = newSen.split(keyList[i-1])                                    #split str on TEMPLATE

       newSen = spl[0] + ansDict[keyList[i-1]] + spl[1]                    #insert user answer between splitted str fragments

    return newSen

sentenceFile = open('sentence.txt','r')                                    

sentence = sentenceFile.read() 

sentenceFile.close()

print(sentence)

#TODO ask user to define swaps for NOUN, ADJECTIVE, VERB and ADVERB

words = {'NOUN':'','ADJECTIVE':'','VERB':'','ADVERB':''}                   #dict holds templates tied to user answers

print('Provide noun:')
words['NOUN'] = input()

print('Provide adjective:')
words['ADJECTIVE'] = input()

print('Provide verb:')
words['VERB'] = input()

print('Provide adverb:')
words['ADVERB'] = input()


#TODO find those in text and swap them with user definitions


keysList = list(words.keys())                                               #Convert keys to list of keys

finalMess = swaper(keysList, words, sentence)                               #Cal swaper function

#TODO print the results

print()
print(finalMess)

