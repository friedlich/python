import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# 一、透视表(pivotTab)
# 透视表就是将指定原有DataFrame的列分别作为行索引和列索引，然后对指定的列应用聚集函数(默认情况下式mean函数)。

df = DataFrame({'类别':['水果','水果','水果','蔬菜','蔬菜','肉类','肉类'],
                '产地':['美国','中国','中国','中国','新西兰','新西兰','美国'],
                '水果':['苹果','梨','草莓','番茄','黄瓜','羊肉','牛肉'],
               '数量':[5,5,9,3,2,10,8],
               '价格':[5,5,10,3,3,13,20]})
print(df)

# 1.按‘产地’和‘类别’重新索引，然后在‘价格’和‘数量’上执行mean函数
print(df.pivot_table(index=['产地','类别']))

print(df.pivot_table(columns=['产地','类别']))

# 2.行索引为‘产地’，列索引为‘类别’，对‘价格’应用‘max’函数，并提供分项统计，缺失值填充0
print(df.pivot_table('价格',index='产地',columns='类别',aggfunc='max',margins=True,fill_value=0))


# 二、交叉表(crossTab)
# 交叉表是用于统计分组频率的特殊透视表
print(pd.crosstab(df['类别'],df['产地'],margins=True)) # 按类别分组，统计各个分组中产地的频数
