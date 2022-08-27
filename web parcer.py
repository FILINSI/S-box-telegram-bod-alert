from ast import While
from cgitb import text
from ssl import AlertDescription
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import time
import telebot

# зациклить код до тех пор пока не будет найден нужный товар
while True:
    link = "https://asset.party/get/developer/preview"
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.Session() as s:
        soup = BeautifulSoup(webpage, 'html5lib')
    print (soup.find('span', attrs={'class':'tag'}).get_text())

    # если началась раздача, заканчиваем программу 
    if soup.find('span', attrs={'class':'tag'}).get_text() != 'key 0':
        print ('Раздача началась')
        
    time.sleep(1) 

    if soup == 'key ':
       time.sleep (500)
    else:
        time.sleep(0)
