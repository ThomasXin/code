# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests
import random
from ip_pool import ip_list
ips = []
for ip in ip_list.split('\n'):
    ips.append(ip)
url = 'http://ip.chinaz.com/'
proxies = {random.choice(ips).split(':')[0]: random.choice(ips)}

r = requests.get(url, proxies=proxies)
soup = BeautifulSoup(r.text, 'lxml')
parent_node = soup.find(class_="IpMRig-tit")
for i in parent_node.find_all('dd'):
    print(i.get_text())



