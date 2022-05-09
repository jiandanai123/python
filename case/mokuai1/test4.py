import requests
from bs4 import BeautifulSoup

# html = open("index.html")
# print(html)
# soup = BeautifulSoup(html,"html.parser")
# #print(soup)
#print(soup.prettify())
# print(soup.body)
# print(type(soup.body))    

#通过查找子元素
# b = soup.find_all("a")
# print(b)
# a = soup.find(class_= "yoyo")
# print(a.contents)

#图片下载

r = requests.get("http://localhost:15001")
print(r.content)
soup = BeautifulSoup(r.content,"html.parser")
soup.find_all("data-v-5958913a")


