# coding: utf-8

# import requests
from bs4 import BeautifulSoup


# url = 'http://www.pythonscraping.com/pages/page3.html'

html = "";
with open('/Users/xiaozefeng/git-repo/learn-crawler/demo/page3.html','r') as f:
    for line in f.readlines():
        html+=line

# next_siblings 获取后面的兄弟节点
# previous_siblings 获取前面的兄弟节点
bsObj = BeautifulSoup(html, "html.parser")
for sibling in bsObj.find('table',{"id":"giftList"}).tr.next_siblings:
    print(sibling)

# parent 或 parents 
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())



