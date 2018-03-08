# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:04:00 2018

@author: zhangyu
"""
'''
aibiy短租租房信息爬取
标题 地址 租金 房源图片链接 房东图片链接 房东性别 名字
#room > div > div._qmx5s9 > div > div > div._2h22gn > div._1kzvqab3 > div > div > div > div > div > section > div._b1aaqf > div > div > div > div > div > div > div > div > div > span
state:#details > div > div > div > div:nth-child(1) > div:nth-child(2) > div > div._79dbpfm > div > div
    #details > div > div > div > div:nth-child(1) > div:nth-child(2) > div > div._79dbpfm > div
    <img alt="" src="https://restapi.amap.com/v3/staticmap?key=a7708a7c3c84313afa7ac50b3cdf0bf7&amp;location=116.4382,39.94613&amp;zoom=13&amp;size=494*280" style="width: 100%;">
#listing-9040671 > div > div._v72lrv > div > a > div > div > div > div._ncmdki > div > span > span > span
grade = #reviews > div > div > div > div > div._xofrn3w > div > div > div > span > div > div > div > span
#room > div > div._qmx5s9 > div > div > div._2h22gn > div._1av41w02 > div > div > div > div > div > div._gor68n > div > div > div:nth-child(1) > div._1wqfqyj > div > div > div > div._10ejfg4u > div > div > div > span 
'''
from bs4 import BeautifulSoup
import requests
url = "https://zh.airbnb.com/rooms/9040671?location=%E5%8C%97%E4%BA%AC%2C%20%E4%B8%AD%E5%9B%BD&s=KCVbsR4A"
urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(1,5)]

def crawl_single(url):
    web_data = requests.get(url)
    code = requests.get(url).status_code
    if(code == 200):
        print("状态正常",code)
        soup = BeautifulSoup(web_data.text,'lxml')
        titles = soup.select("#room > div > div._qmx5s9 > div > div > div._2h22gn > div > div > div > div > div > div > section > div._b1aaqf > div > div > h1")
        infos = soup.select("#room > div > div._qmx5s9 > div > div > div._2h22gn > div._1kzvqab3 > div > div > div > div > div > section > div._b1aaqf > div > div > div > div > div > div > div > div > div > span")
        states = soup.select("#details > div > div > div > div > div > div > div._79dbpfm > div")
        #images = soup.select("#room > div > div > div > div > div > div > div > div > span > span > img")
        #prices = soup.select("#room > div > div._qmx5s9 > div > div > div._2h22gn > div._1av41w02 > div > div > div > div > div > div._gor68n > div > div > div > div._1wqfqyj > div > div > div > div._10ejfg4u > div > div > div > span")
        grades = soup.select("#reviews > div > div > div > div > div._xofrn3w > div > div > div > span > div > div > div > span")
        infoList = []                  
        for info in infos:
            infoList.append(info.text)
        print(titles[0].text)
        print("状态：",states[0].text)
       # print(images[0].get('src'))
        #print(grades.get('aria-label'))
        #print(prices)
        print("评价等级",grades[0].get('aria-label')) 
        print("房间详情：",infoList)
    else:
        print("连接失败",code)
        
        
crawl_single(url)
