# coding :utf-8
import requests
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    res = requests.get("http://en.wikipedia.org"+pageUrl)
    bs = BeautifulSoup(res.text, "html.parser")
    try:
        print(bs.h1.get_text())
        print(bs.find(id="mw-content-text").findAll("p")[0])
        print(bs.find(id="ce-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("this page is missing some attribute! No worries though")
    
    for link in bs.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-----------\n %s \n" % newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")