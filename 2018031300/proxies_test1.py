# _*_ coding:utf-8 _*_
import random
import requests
from proxy import GainProxies
from bs4 import BeautifulSoup
gain = GainProxies()
ips = []
for ip in gain.get_ip_list():
    ips.append(ip)
url = 'http://ip.chinaz.com/'
proxies = {random.choice(ips).split(':')[0]: random.choice(ips)}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

r = requests.get(url, headers=headers, proxies=proxies)
soup = BeautifulSoup(r.text, 'lxml')
parent_node = soup.find(class_="IpMRig-tit")
for i in parent_node.find_all('dd'):
    print(i.get_text())



