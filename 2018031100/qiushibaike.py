# _*_ coding:utf-8 _*_

import json
import requests
# 使用了线程库
import threading
from Queue import Queue
from lxml import etree


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        # 线程名
        self.threadName = threadName
        # 页码队列
        self.pageQueue = pageQueue
        # 解析结果队列
        self.dataQueue = dataQueue

        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    def run(self):
        print '启动' + self.threadName
        while not CRAWL_EXIT:
            try:
                # 取出一个数字，先进先出。
                # 可选参数block,默认值为True
                # 1.如果队列为空，block为True的话，不会结束，就会进入阻塞状态，知道队列有新的数据
                # 2.如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
                page = self.pageQueue.get(False)
                url = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'

                r = requests.get(url, headers=self.headers)
                # print r.content
                self.dataQueue.put(r.content)
            except:
                pass
        print '结束' + self.threadName


class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename

    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse1(html)
                # print html
            except:
                pass

    def parse1(self, html):

        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')
        items = {}
        for node in node_list:
            # xpath返回列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/h2')[0].text
            # 图片；链接
            image = node.xpath('.//div[@class="thumb"]//@src')
            # 段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comment = node.xpath('.//i')[1].text

            items = {
                'username': username,
                'image': image,
                'content': content,
                'zan': zan,
                'comment': comment
            }

            self.filename.write(json.dumps(items, ensure_ascii=False).encode('utf-8'))


CRAWL_EXIT = False
PARSE_EXIT = False
def main():
    # 页码的队列，表示10个页面
    pageQueue = Queue(10)
    # 放入1~10的数字，先进先出
    for page in range(1, 11):
        pageQueue.put(page)
    # 采集结果的数据队列，参数为空表示不限制
    dataQueue = Queue()

    filename = open("duanzi.json", 'a')



    # 三个采集线程的名字
    crawlList = ["采集线程一号", "采集线程二号", "采集线程三号"]
    # 存储三个采集线程的名字
    threadcrawl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)



    # 三个解析线程的名字
    parseList = ['解析线程一号', '解析线程二号', '解析线程三号']
    # 存储三个解析线程的名字
    threadparse = []

    for threadName in parseList:
        thread = ThreadParse(threadName, dataQueue, filename)
        thread.start()
        threadparse.append(thread)



    # 等待pageQueue队列为空，也就是等待之前的操作执行完毕
    while not pageQueue.empty():
        pass
    # 如果pageQueue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print "pageQueue为空"

    while not dataQueue.empty():
        pass
    global PARSE_EXIT

    PARSE_EXIT = True


    for thread in threadcrawl:
        thread.join()
        print '1'


if __name__ == "__main__":
    main()