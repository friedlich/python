# 思路：numpy提供了numpy.concatenate((a1,a2,...), axis=0)函数。能够一次完成多个数组的拼接。其中a1,a2,...是数组类型的参数
import numpy as np

a = np.array([1, 2, 3])
b = np.array([11, 22, 33])
c = np.array([44, 55, 66])
print(np.concatenate((a, b, c), axis=0))  # 默认情况下，axis=0可以不写
# print(np.concatenate((a, b, c), axis=1))
# array([1, 2, 3, 11, 22, 33, 44, 55, 66])  # 对于一维数组拼接，axis的值不影响最后的结果

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,21,31],[7,8,9]])
print(np.concatenate((a,b),axis=0))

print(np.concatenate((a,b),axis=1)) #axis=1表示对应行的数组进行拼接