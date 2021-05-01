#! python3
#Opens google maps on address provided via console or from clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
   
    address = ' '.join(sys.argv[1:]) 
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.pl/maps/place/' + address)