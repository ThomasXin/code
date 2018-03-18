# _*_ coding:utf-8 _*_


import json
import time
import requests
import jsonpath
from lxml import etree
from selenium import webdriver

import pandas as pd
class MeiZiTu():

    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def loadPage(self):

        source = requests.get(self.url, headers=self.headers)

        unicodestr = json.loads(source.text)
        print unicodestr
        lists = jsonpath.jsonpath(unicodestr, '$..userid')
        for node in lists:
            infourl = 'http://www.lovewzly.com/user/' + node + '.html'
            print infourl
            self.meinvinfo(infourl)
    def meinvinfo(self, url):
        source = requests.get(url, headers=self.headers)
        time.sleep(1)
        html = etree.HTML(source.text)
        try:
            for imgurl in html.xpath('//ul[@class= "clearfix"]/li/img/@src'):
                dataframe = pd.DataFrame({'imgurl': imgurl}, index=[0])
                dataframe.to_csv('meizi.csv', index=False, sep=',', mode='a')
        except:
            pass
if __name__ == '__main__':
    offset = 1
    while True:
        if offset < 10000:
            time.sleep(2)
            url = 'http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&startheight=161&endheight=170&marry=1&page=%s' % str(offset)
            mzt = MeiZiTu(url)
            mzt.loadPage()
            offset += 1
        else:
            break
