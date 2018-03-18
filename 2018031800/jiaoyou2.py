# _*_ coding:utf-8 _*_
import charts
import pandas as pd


source = pd.read_csv(r'C:\Users\Administrator\Desktop\pc\2018031800\info.csv')
# 1
province_list =[]
for city in source['province'].replace('province', ''):
    province_list.append(city)
city_index = list(set(province_list))

print len(city_index)
post_times =[]
for index in city_index:
    post_times.append(province_list.count(index))
print post_times
def data_gen(types):
    length = 0
    if length <= len(city_index):
        for typed, num in zip(city_index, post_times):
            data = {
                'name': typed,
                'data': [num],
                'type': types
            }
            yield data
            length += 1
series = [data for data in data_gen('gauge')]
charts.plot(series, show='inline', options=dict(title=dict(text='xxx')))