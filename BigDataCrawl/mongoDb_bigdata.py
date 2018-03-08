from bs4 import BeautifulSoup
import requests
import time
import pymongo

url = "https://zh.airbnb.com/s/%E5%8C%97%E4%BA%AC/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=_blAqeQy&section_offset=1&cdn_cn=1"
#url列表
urls = ["https://zh.airbnb.com/s/%E5%8C%97%E4%BA%AC/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=_blAqeQy&section_offset={}".format(str(i)) for i in range(3, 31)]
#连接mongoDB数据库
client = pymongo.MongoClient('localhost', 27017)
aibiy = client['aibiy']
sheet_lines = aibiy['sheet_lines']

def crawl_single(url):
    web_data = requests.get(url)
    #多睡会，防止封ip
    time.sleep(3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    #通过属性名查找
    titles = soup.find_all("meta", itemprop="name")
    #通过子标签查找
    #titles = soup.select("div > div._v72lrv > div > a > div > div > div")
    prices = soup.select("div > div._v72lrv > div > a > div > div > div > div._ncmdki > div > span > span > span > span > span")
    infos = soup.select("div > div._v72lrv > div > a > div > div > small > div")
    grades = soup.select("div > div._v72lrv > div > a > div > div > div > span._q27mtmr > span")

    #价格加工列表，把"价格"删除
    a = []
    for price in prices:
        if price.get_text() != "价格":
            a.append(price)

    #确定标题长度与其他相同
    newTitle = []
    for i in range(len(infos)):
        newTitle.append(titles[i])
    #添加到字典
    for title, price, info, grade in zip(newTitle, a, infos, grades):
        data = {
        	#转为字符串，把前后不要的部分去掉
            'title': str(title).replace("<meta content=\"", "").replace("\" itemprop=\"name\"/>", ""),
            'price': price.get_text(),
            'info': info.get_text(),
            'grade': grade.get("aria-label"),
        }
        print(data)
        sheet_lines.insert_one(data)
    print("done")

for url in urls:
    i = 1
    crawl_single(url)
    print("第", i, "页成功")
    i = i + 1
    