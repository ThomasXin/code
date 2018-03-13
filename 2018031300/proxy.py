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
        web_data = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(web_data.text, 'lxml')

        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[5].text + '://' + tds[1].text + ':' + tds[2].text)
        return ip_list