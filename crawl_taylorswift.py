# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:17:57 2018

@author: zhangyu68
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
import time

pro_url = "http://weheartit.com/inspirations/beach?page="
path = "D:/PythonCode/爬虫/爬虫test/meimeiPIC"


def get_image_url(num):
    img_urls = []
    #给定爬取开始点
    for page_num in range(10,10+num):
        full_url = pro_url+str(page_num)
        web_data = requests.get(full_url)
        time.sleep(2)
        soup = BeautifulSoup(web_data.text,'lxml')
        images = soup.select('#main-container > div.grid-responsive > div.col.span-content > div > div > div > div > div > a > img')
        for i in images:
            img_urls.append(i.get('src'))
    print(len(img_urls),"pictures shall be downloaded")
    return img_urls

'''
Copy a network object denoted by a URL to a local file, 
if necessary. If the URL points to a local file, 
or a valid cached copy of the object exists, 
the object is not copied. Return a tuple (filename, headers) where filename is the local file name under which the object can be found,
 and headers is whatever the info() method of the object returned by urlopen() returned (for a remote object, possibly cached). Exceptions are the same as for urlopen().
 urllib.urlretrieve(url[, filename[, reporthook[, data]]])
 
'''
def dl_images(url):
    urllib.request.urlretrieve(url,path+url.split('/')[-2] + url.split('/')[-1])
    print("Done")
    

#给定爬取页数
for url in get_image_url(2):
    dl_images(url)
    
