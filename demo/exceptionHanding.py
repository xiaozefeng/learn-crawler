# coding: utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
        return None

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("title could not be found")
else:
    print(title)