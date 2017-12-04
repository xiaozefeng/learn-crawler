# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
res = requests.get(url)
bs = BeautifulSoup(res.text, "html.parser")
allText = bs.findAll(id="text")
print(allText[0].get_text())