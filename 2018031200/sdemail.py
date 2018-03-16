# _*_ coding:utf-8 _*_

import re
import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


class SendEmail():
    """
        作用：
            1.本程序是给指定的邮箱发送邮件。
            2.随机生成6位验证码
            3.发件人邮箱，需开启SMTP设置 。教程在这： https://jingyan.baidu.com/article/295430f1fc28a60c7e0050f9.html
            4.解决python发邮件乱码问题。教程在这：http://blog.csdn.net/zm2714/article/details/8134118
    """
    def __init__(self, to_addr):
        # 发件人邮箱
        self.from_addr = 'sssssssss@sina.com'
        # 邮箱密码
        self.password = 'xxxxxx'

        # 收件人邮箱
        self.to_addr = to_addr
        # 'xihulu_job@163.com'
        self.smtp_server = 'smtp.sina.com'
    def _format_addr(self,s):

        name, addr = parseaddr(s)

        return formataddr((Header(name, 'utf-8').encode(), addr))

    def random_verification(self):

        code_list = []

        for i in range(10): # 0-9
            code_list.append(str(i))
        for i in range(65, 91): # A-Z
            code_list.append(chr(i))
        for i in range(97, 123): # a-z
            code_list.append(chr(i))
        # 随机在数组里面选择6个
        myslice = random.sample(code_list, 6)
        # 将他们进行拼接得到字符串
        verification_code = ''.join(myslice)

        return verification_code
    def subject(self):
        # 正文
        msg = MIMEText('您的验证码是：%s' % self.random_verification() ,_charset="utf-8")
        # 发件人
        msg['from'] = self._format_addr('郡主阁<%s>' % self.from_addr)
        # 收件人
        msg['to'] = self._format_addr('邪公子<%s>' % self.to_addr)
        # 主题
        msg['subject'] = Header('人事安排', 'utf-8').encode('utf-8')


        server = smtplib.SMTP(self.smtp_server, 25)

        server.login(self.from_addr, self.password)

        server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        print '已发送'
        server.quit()
class InputYourToEmail():
    """
        这个类，是为了检测你输入的邮箱地址是否符合规范
    """
    def input_your_email(self):
        __author__ = '醉梦红尘'
        flag = True
        while flag:
            text = raw_input("Please input your Email address：\n")
            if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
            #if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
                print('Email address is Right!')
                flag = False
                return text
            else:
                print('Please reset your right Email address!')

if __name__ == '__main__':

    iyte = InputYourToEmail()
    toaddr =iyte.input_your_email()
    sd = SendEmail(toaddr)

    sd.subject()









