#!/usr/bin/env python
#_*_coding:utf-8_*_

"""
本文利用，selenium, bs4, re
解决js 爬虫问题。
使用库方面，感谢ipython提供的开发提示和官网文档
bs4, 其利用tree xml结构对其网页进行解析，有很多查找节点的函数。非常好定位节点。
re, 其可以抽取文本中，想要的信息，特别是利用search， groups的方法。分区查找。
driver, 这个库，可以提供节点查找和定位节点属性和方法，利用交互式爬虫。其中，数据同步的问题很重要。
time, 这个库，可以计算程序执行时间，程序等待等问题，trick方式解决等待。
另一点：python里面最好不要写while 循环。
"""


from selenium import webdriver
from bs4 import BeautifulSoup

import urllib
import urllib.request
import re
import time
import sys


driver = webdriver.PhantomJS()
url = 'http://talk.kekenet.com/list_11'
driver.get(url)
data = driver.page_source

a_pattern = re.compile(r'(<dt><span class="j_num">a</span>)(.*)(<p>.*</p></dt>)')
b_pattern = re.compile(r'(<dd><span class="j_num">b</span>)(.*)(<p>.*</p></dd>)')
button = re.compile(r'^[0-9]+$')

usoup = BeautifulSoup(data, 'xml')
div = usoup.find('div', {'class':'clear_div left_nav_c blue_bj'})
all_li = div.find_all('li')

all_cat = list()
for li in all_li:
    ahref = li.find('a')
    all_cat.append(ahref.attrs['href'])

for url in all_cat:
    driver.get(url)
    data = driver.page_source
    clicked = set()
    clicked.add("1")
    print(url, "1")
    while True:
        for line in data.split('\n'):
            match = re.search(a_pattern, line)
            if match:
                print('Q\t', match.groups()[1])
            match = re.search(b_pattern, line)
            if match:
                print('A\t', match.groups()[1])
        lst = driver.find_elements_by_xpath('//div[@class="clear_div page"]/a')
        if lst and len(lst) > 0:
            index = 0
            text = lst[index].text
            while (text in clicked or button.match(text) is None) and index < len(lst) - 1:
                index += 1
                text = lst[index].text
            if index < len(lst) and text not in clicked:
                clicked.add(text)
                try:
                    lst[index].click()
                    time.sleep(5)
                    print(url, text)
                    data = driver.page_source
                except Exception as e:
                    driver.save_screenshot('screenshot.png')
                    continue
            else:
                break
        else:
             break
