from ast import While
from cgitb import text
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import time
''''Кодировка для получения данных из сайта'''
# зациклить код до тех пор пока не будет найден нужный товар
while True:
    link = "https://asset.party/get/developer/preview"
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.Session() as s:
        soup = BeautifulSoup(webpage, 'html5lib')
    print (soup.find('span', attrs={'class':'tag'}).get_text())

    time.sleep(1)

    # если началась разжача, заканчиваем программу 
    if soup.find('span', attrs={'class':'tag'}).get_text() != 'key 0':
        break
    else:
        continue
