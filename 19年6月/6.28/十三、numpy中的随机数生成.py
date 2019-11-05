import numpy

print('numpy.random随机数生成')
import numpy.random as npr

x = npr.randint(0,2,size=100000) #抛硬币
print((x>0).sum()) # 正面的结果
print(npr.normal(size=(2,2))) #正态分布随机数数组 shape = (2,2)
