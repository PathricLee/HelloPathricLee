#!/usr/bin/python
#_*_coding=utf-8_*_

from urllib.parse import quote
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()

def query_baidu_news(keyword):
    url = u'http://news.baidu.com/ns?word=' +quote(keyword) +'&tn=news&from=news&cl=2&rn=20&ct=1'
    driver.get(url)
    data = driver.page_source

    usoup = BeautifulSoup(data, 'lxml')
    results = usoup.find_all(class_='result')
    for r in results:
        a = r.find('a')
        title = a.text.strip()
        print('\t'.join([keyword, title]))

def query_toutiao_news(keyword):
    url = u'https://www.toutiao.com/search/?keyword=' +quote(keyword)
    driver.get(url)
    data = driver.page_source

    usoup = BeautifulSoup(data, 'lxml')
    results = usoup.find_all(class_='link title')
    print(len(results))
    for r in results:
        a = r.find('a')
        title = r.text.strip()
        #print('\t'.join([keyword, title]))
        print(title)

if __name__ == '__main__':
    query_toutiao_news('机构盘点')
