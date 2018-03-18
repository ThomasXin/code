# _*_ coding:utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import json
import time
import requests
import jsonpath
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

        lists = jsonpath.jsonpath(unicodestr, '$..list')
        for info in lists[0]:
            data = {

             		 'province': info['province'],
                     'city':  info['city'],
                     'gender': info['gender'],
                     'monolog':  info['monolog'],
                     'userid':  info['userid'],
                     'height':  info['height'],
                     'username':  info['username'],
                     'avatar':  info['avatar'],
                     'education':  info['education'],
                     'birthdayyear':  info['birthdayyear']
            }
            print info['monolog']

            dataframe = pd.DataFrame(data=data, index=[0])

            dataframe.to_csv('info.csv', index=False, sep=',', mode='a')



if __name__ == '__main__':
    offset = 1
    while True:
        if offset < 10000:
            time.sleep(2)
            # url = 'http://www.lovewzly.com/api/user/pc/list/search?gender=2&cityid=52&startheight=161&endheight=170&marry=1&page=%s' % str(offset)
            url = 'http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&startheight=161&endheight=170&marry=1&page=%s' % str(offset)
            mzt = MeiZiTu(url)
            mzt.loadPage()
            offset += 1
        else:
            break
