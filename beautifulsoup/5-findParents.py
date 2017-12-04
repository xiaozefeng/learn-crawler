# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')

print(bs.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
