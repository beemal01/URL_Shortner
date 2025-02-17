
#Installl these 2 pip from your terminal
# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input("Enter your URL: ")

def shortenURL(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenURL(url)