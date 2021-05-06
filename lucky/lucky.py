#! python3
#Open few new tabs in chrome to with search results of command interface arguments

import sys, requests, webbrowser, logging, bs4
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)

logging.debug('Program start')

resPage = requests.get('http://www.google.com/search?q=' + '+'.join(sys.argv[1:]))                                                   #Download result page

resPage.raise_for_status                                                                                                             #Raise exception if no page found

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#DEB checks

logging.debug(type(resPage))                                                    #DEB Response obj check                                                                                      

logging.debug('status_code: ' + str(resPage.status_code == requests.codes.ok))  #DEB Check status_code

logging.debug(len(resPage.text))                                                #DEB size of downloaded result page

#End DEB checks
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

soup = bs4.BeautifulSoup(resPage.text, 'html.parser')                                                                                   #Create bs4 object

logging.debug('BS4 object check: ' + str(type(soup)))                           #DEB BH4 proper obj check



logging.debug(soup.prettify())                                                  #DEB for makeing out soup structure

links = soup.select('.kCrYT a')

logging.debug(links)                                                            #DEB Check structure of selected fragments of soup

numOpen = min(5,len(links))                                                                                                             #For minimal number of search results

for i in range(numOpen):                                                                                                                #Open new tab in chrome for numOpen links
    webbrowser.open('http://google.pl' + links[i].get('href'))


logging.debug('Program end')

