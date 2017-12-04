# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://baidu.com")
res = html.read().decode('utf-8')
bsObj = BeautifulSoup(res,'html.parser')
print(bsObj.title)