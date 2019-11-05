import numpy

print('ndarray的布尔型索引')
x = numpy.array([3,2,3,1,3,0])
# 布尔型数组的长度必须跟被索引的轴长度一致
y = numpy.array([True,False,True,False,True,False]) 
print(x[y]) # [3,3,3] 
print(x[y==False]) # [2,1,0]
print(x>=3) # [ True False  True False  True  False]
print(x[~(x>=3)]) # [2,1,0]
print((x==2)|(x==1)) # [False  True False  True False False]
print(x[(x==2)|(x==1)]) # [2 1]
x[(x==2)|(x==1)] = 0
print(x) # [3 0 3 0 3 0]

print('ndarray的花式索引:使用整型数组作为索引')
x = numpy.array([1,2,3,4,5,6])
print(x[[0,1,2]]) # [1 2 3]
print(x[[-1,-2,-3]]) # [6,5,4]
x = numpy.array([[1,2],[3,4],[5,6]])
print(x)
print(x[[0,1]]) # [[1,2],[3,4]]
print(x[[0,1],[0,1]]) # [1,4] 打印x[0][0]和x[1][1]
print(x[[0,1]][:,[0,1]]) # 打印01行的01列 [[1,2],[3,4]] 
# 使用numpy.ix_()函数增强可读性
print(x[numpy.ix_([0,1],[0,1])]) #同上 打印01行的01列 [[1,2],[3,4]]
x[[0,1],[0,1]] = [0,0]
print(x) # [[0,2],[3,0],[5,6]]
