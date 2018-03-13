# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

class GainProxies():
    """
        作用：此程序是为了在西刺代理获取免费的代理ip
    """
    def __init__(self):
        self.url = 'http://www.xicidaili.com/nn/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    def get_ip_list(self):
        # 发送请求
        web_data = requests.get(self.url, headers=self.headers)
        # 获取源码
        html = web_data.text
        # 用‘lxml’解析
        soup = BeautifulSoup(html, 'lxml')
        # 找出所有的‘tr’，返回的是一个列表
        ips = soup.find_all('tr')
        # 创建数组
        ip_list = []
        for i in range(1, len(ips)):
            # 将ips里面的每一项分别赋值给ip_info
            ip_info = ips[i]
            # 找出每一项里面的所有td
            tds = ip_info.find_all('td')
            # 将我们需要的每一项取出来，
            ip_list.append(tds[5].text + '://' + tds[1].text + ':' + tds[2].text)
        return ip_list