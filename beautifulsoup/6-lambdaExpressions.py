# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page2.html"
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')

tags = bs.findAll(lambda tag: len(tag.attrs) ==2)
for tag in tags:
    print(tag)
