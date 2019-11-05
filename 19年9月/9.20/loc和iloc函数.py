# 1. 利用loc、iloc提取行数据
import numpy as np
import pandas as pd
#创建一个Dataframe
data = pd.DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('ABCD'))
print(data)
print(data.loc['a', :])
print(data.iloc)
print(data.iloc[0, :])

# 2. 利用loc、iloc提取列数据
print(data.loc[:,['A']]) #取'A'列所有行，多取几列格式为 data.loc[:,['A','B']]
print(data.iloc[:,[0]]) #取第0列所有行，多取几列格式为 data.iloc[:,[0,1]]

# 3.利用loc、iloc提取指定行、指定列数据
print(data.loc[['a','b'],['A','B']]) #提取index为'a','b',列名为'A','B'中的数据
print(data.iloc[[0,1],[0,1]]) #提取第0、1行，第0、1列中的数据

# 4.利用loc、iloc提取所有数据
print(data.loc[:,:]) #取A,B,C,D列的所有行
print(data.iloc[:,:]) #取第0,1,2,3列的所有行

# 5.利用loc函数，根据某个数据来提取数据所在的行
print(data.loc[data['A']==0]) #提取data数据(筛选条件: A列中数字为0所在的行数据)
print(data.loc[(data['A']==0)&(data['B']==1)]) #提取data数据(多个筛选条件)