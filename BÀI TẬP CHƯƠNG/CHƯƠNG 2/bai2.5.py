import requests
import xml.dom.minidom
import csv
url = 'https://www.hindustantimes.com/feeds/rss/entertainment/music/rssfeed.xml'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
source=requests.get(url, headers=headers)
with open('ex.xml', 'wb') as f: 
        f.write(source.content)
doc = xml.dom.minidom.parse("ex.xml")
news = []
for x in doc.getElementsByTagName("title"):
    news.append({x.firstChild.nodeValue:''})
b = doc.getElementsByTagName('description')
b = list(b)
news2 = []
for a in range(0,len(b)) :
    dict_values = dict.fromkeys(news[a],b[a].firstChild.nodeValue)
    news2.append(list(dict_values))
with open("news.csv",'a') as f:
    for i in news2:
         csv.writer(f).writerow(i)