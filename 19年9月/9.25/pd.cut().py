# cut将根据值本身来选择箱子均匀间隔，即每个箱子的间距都是相同的

import numpy as np
import pandas as pd

factors = np.random.randn(9)
print(factors)

# 传入bins参数
pd.cut(factors, 3) #返回每个数对应的分组
print(pd.cut(factors, 3))
pd.cut(factors, bins=[-3,-2,-1,0,1,2,3])
print(pd.cut(factors, bins=[-3,-2,-1,0,1,2,3]))
pd.cut(factors, 3).value_counts()  # 计算每个分组中含有的数的数量
print(pd.cut(factors, 3).value_counts())

# 传入lable参数
pd.cut(factors, 3,labels=["a","b","c"]) #返回每个数对应的分组，但分组名称由label指示
print(pd.cut(factors, 3,labels=["a","b","c"]))
pd.cut(factors, 3,labels=False) #返回每个数对应的分组，但仅显示分组下标
print(pd.cut(factors, 3,labels=False))
# 传入retbins参数
pd.cut(factors, 3,retbins=True)# 返回每个数对应的分组，且额外返回bins，即每个边界值
print(pd.cut(factors, 3,retbins=True))

# 参数 	说明
# x 	array，仅能使用一维数组
# bins 	integer或sequence of scalars，指示划分的组数或指定组距
# labels 	array或bool，默认为None。当传入数组时，分组的名称由label指示；当传入Flase时，仅显示分组下标
# retbins 	bool，是否返回bins，默认为False。当传入True时，额外返回bins，即每个边界值。
# precision 	int，精度，默认为3
