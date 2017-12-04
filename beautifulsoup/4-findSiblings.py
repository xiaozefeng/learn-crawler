# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')

for siblings in bs.find("table", {"id":"giftList"}).tr.next_siblings:
    print(siblings)
