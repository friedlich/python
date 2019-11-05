# loc——通过行标签索引行数据
# iloc——通过行号索引行数据
# ix——通过行标签或者行号索引行数据（基于loc和iloc 的混合）

# 分别使用loc、iloc、ix 索引多列的数据:
import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['a','b']  # 行号
columns = ['c','d','e']  # 列号
df = pd.DataFrame(data,index=index,columns=columns)  # 生成一个数据框
print(df)
print(df.loc[:,'c':'d'])
print(df.iloc[:,0:2])
print(df.ix[:,'c':'d'])
print(df.ix[:,0:2])
