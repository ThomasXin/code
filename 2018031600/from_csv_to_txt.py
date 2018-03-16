# _*_ coding:utf-8 _*_

import pandas as pd
filename = pd.read_csv(r'C:\Users\Administrator\Desktop\pc\2018031600\test.csv')
# 遇到数据中含有‘_’就会报错
# TypeError: The numpy boolean negative, the `-` operator, is not supported, use the `~` operator or the logical_not function instead.
print filename

#    a_name  b_name
# 0       1       4
# 1       2       5
# 2       3       6
#
# [3 rows x 2 columns]