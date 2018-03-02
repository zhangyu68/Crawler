# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:25:18 2018

@author: zhangyu68
"""

from bs4 import BeautifulSoup

with open('D:/学习/Python实战：四周实现爬虫系统/课程资料/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html','r') as data:
   #print(data)
   Soup = BeautifulSoup(data,'lxml')
   #print(Soup)
   titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")
   images = Soup.select("body > div > div > div.col-md-9 > div > div > div > img")
   prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
   grades_crawler = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2) > span ")
   #print(grades_crawler)
   grades = []
   

   while len(grades_crawler) !=0:
       e = grades_crawler[0:5]
       grades.insert(1,e)
       del grades_crawler[0:5]

for title, image, price, grade in zip(titles, images, prices, grades):
    star = []
    b = str(grade)  # 字符串化列表
    c = b.replace('<span class="glyphicon glyphicon-star"></span>', '★')  # 将描述实五角星的替换为图案
    d = c.replace('<span class="glyphicon glyphicon-star-empty"></span>', '☆')  # 将描述虚五角星的替换为图案
    star.append(d)  # 将转化完的结果逐个插入列表star中
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'price': price.get_text(),
        'grade': ''.join(star).replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
    }
    print(data)
   
