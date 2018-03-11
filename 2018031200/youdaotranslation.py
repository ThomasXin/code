# _*_ coding:utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import urllib
import urllib2

word = raw_input('Please enter the word you are looking for:')

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=ugc"
headers = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
fromdata = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1520784936914",
    "sign": "8ed84af2f01d51d28dadf4cf76ce7d6e",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false",
}

data = urllib.urlencode(fromdata)

request = urllib2.Request(url, data=data, headers=headers)

response = urllib2.urlopen(request)
sourse = response.read()
html = json.loads(sourse)
result = html['translateResult'][0][0]['tgt']
wordcount = {
    11: result
}
with open('word.txt', 'a') as f:
    f.write(word + ':\t')
    f.write(result + '\n')
print html['translateResult'][0][0]['tgt']