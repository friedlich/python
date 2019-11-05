import numpy as np
import pandas as pd

factors = np.random.randn(12)
print(factors)

# pd.qcut()
# qcut是根据这些值的频率来选择箱子的均匀间隔，即每个箱子中含有的数的数量是相同的

# 传入q参数
pd.qcut(factors, 3) #返回每个数对应的分组
print(pd.qcut(factors, 3))
pd.qcut(factors, 3).value_counts() #计算每个分组中含有的数的数量
print(pd.qcut(factors, 3).value_counts())

# 传入lable参数
pd.qcut(factors, 3, labels=["a", "b", "c"])  # 返回每个数对应的分组，但分组名称由label指示
print(pd.qcut(factors, 3, labels=["a","b","c"]))
pd.qcut(factors, 3, labels=False) #返回每个数对应的分组，但仅显示分组下标
print(pd.qcut(factors, 3, labels=False))

# 传入retbins参数
pd.qcut(factors, 3, retbins=True)# 返回每个数对应的分组，且额外返回bins，即每个边界值
print(pd.qcut(factors, 3, retbins=True))


# 参数 	说明
# x 	ndarray或Series
# q 	integer，指示划分的组数
# labels 	array或bool，默认为None。当传入数组时，分组的名称由label指示；当传入Flase时，仅显示分组下标
# retbins 	bool，是否返回bins，默认为False。当传入True时，额外返回bins，即每个边界值。
# precision 	int，精度，默认为3
