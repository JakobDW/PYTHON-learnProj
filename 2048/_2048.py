#Automate playing 2048 game on browser
import bs4, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')


count = 0


while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        retryButton = browser.find_element_by_class_name('retry-button')
        score = browser.find_element_by_class_name('score-container')
        sc = score.text
    
        retryButton.click()
        
        print('End of run number:  %s' %str(count + 1))
        print('Score: ' + str(sc))
        
        count+=1

    except:
        print('', end ='')
    
        
    if count == 5:
        break
       


    
