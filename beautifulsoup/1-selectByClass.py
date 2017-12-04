# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'

res = requests.get(url)
bsObj = BeautifulSoup(res.text, 'html.parser')
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name)