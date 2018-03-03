# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 19:07:13 2018

@author: zhangyu
"""


'''
https://www.showstart.com/event/list?cityId=10&isList=1&pageNo=1
https://www.showstart.com/event/list?cityId=10&isList=1&pageNo=2
https://www.showstart.com/event/list?cityId=10&isList=1&pageNo=327
body > div.main.auto-width > ul > li:nth-child(4) > a > div > img
'''
from bs4 import BeautifulSoup
import requests

url = "https://www.showstart.com/event/list?cityId=10&isList=1&pageNo=1"
#找出不同页面的差异性
urls = ["https://www.showstart.com/event/list?cityId=10&isList=1&pageNo={}".format(str(i)) for i in range(1,31)]

def get_attractions(url):
    import time
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select("body > div.main.auto-width > ul > li > a > p.g-name")
    persons = soup.select("body > div.main.auto-width > ul > li > a > p.performerName")
    prices = soup.select("body > div.main.auto-width > ul > li > a > p.g-price > b")
    times = soup.select("body > div.main.auto-width > ul > li > a > p.g-time")
    places = soup.select("body > div.main.auto-width > ul > li > a > p.g-place.a-link")
    images = soup.select("body > div.main.auto-width > ul > li > a > div > img")
    print(images)
    for title,person,price,time,place,imge in zip(titles,persons,prices,times,places,images):
        data = {
                'title':title.get_text().replace("\t","").replace("\n","").replace("独家","").replace("【秀动呈献】",""),
                'person':person.get_text().replace("\t","").replace("\n",""),
                'price':price.get_text(),
                'time':time.get_text().replace("\t","").replace("\n",""),
                'place':place.get_text(),
                'imge':imge.get('original')
             }
        print(data)

for url in urls:
    get_attractions(url)


