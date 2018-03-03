# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 20:36:08 2018

@author: zhangyu
"""

from bs4 import BeautifulSoup
import requests
'''
爬取秀动网站的演出信息 包括演出名，艺人，场地，票价，宣传图
'''
url = 'https://www.showstart.com/host/3598'

web_data = requests.get(url)
#print(web_data.text)
soup = BeautifulSoup(web_data.text,'lxml',from_encoding='utf-8')
#print(soup.original_encoding)
titles = soup.select("#tab3 > div > ul > li > a > p.g-name")
#print(titles)
images = soup.select("#tab3 > div > ul > li > a > div > img")
persons = soup.select("#tab3 > div > ul > li > a > p.performerName")
prices = soup.select("#tab3 > div > ul > li > a > p.g-price > b")
places = soup.select("#tab3 > div > ul > li > a > p.g-place.a-link")
#print(images)
for title,image,person,price,place in zip(titles,images,persons,prices,places):
    data =  {
            'title':title.get_text().replace("\t","").replace("\n","").replace("独家群聊【秀动呈献】",""),
            'image':image.get('original'),
            'person':person.get_text().replace("\t","").replace("\n",""),
            'price':price.get_text(),
            'place':place.get_text()
            }

    print(data)
    
    
    
'''
#tab3 > div > ul > li:nth-child(6) > a > div > img
#tab3 > div > ul > li:nth-child(1) > a > div > div
#tab3 > div > ul > li:nth-child(2) > a > p.g-name
'''
