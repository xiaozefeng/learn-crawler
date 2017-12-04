# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
for child in bs.find("table", {"id":"giftList"}).children:
    print(child)
