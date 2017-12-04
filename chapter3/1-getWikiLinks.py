# coding: utf-8

import requests
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    res = requests.get("http://en.wikipedia.org"+articleUrl)
    bs = BeautifulSoup(res.text, "html.parser")
    return bs.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) >0:
    newArticle = links[random.randint(0, len(links) -1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)