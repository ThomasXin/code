# _*_ coding:utf-8 _*_
import pandas as pd
filename = open(r'C:\Users\Administrator\Desktop\pc\2018030300\GQWM.txt', 'r')

for meinv in filename.readlines():
    name = meinv.split('\t')[0]
    img_link = meinv.split('\t')[1]
    mp4_link = meinv.split('\t')[2]
        # 这个是一个异常,好像必须加一个索引而且还要是数组样式的
        # ValueError: If using all scalar values, you must must pass an index
        # dataframe = pd.DataFrame({'name': name, 'img_link': img_link, 'mp4_link': mp4_link})
    dataframe = pd.DataFrame({'name': name, 'img_link': img_link, 'mp4_link': mp4_link}, index=[0])
    # mode= 'a'是追加，要不然就覆盖只有一行了。通过这里我感觉有什么方法出现问题，还是要看看源码是怎么解释的
    dataframe.to_csv('meinv.csv', index=False, sep=',', mode='a')



