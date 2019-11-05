import numpy
print('线性代数') # 线性代数（linear algebra）
import numpy.linalg as nla   
print('矩阵点乘')
x = numpy.array([[1,2],[3,4]])
print(x)
y = numpy.array([[1,3],[2,4]]) 
print(y)
print(x.dot(y)) # [[ 5 11][11 25]] ### =[(1*1+2*2)+(1*3+2*4)][(3*1+4*2)+(3*3+4*4)]
print(numpy.dot(x,y)) # # [[ 5 11][11 25]]
print('矩阵求逆')
x = numpy.array([[1,1],[1,2]])
y = nla.inv(x) # 矩阵求逆（若矩阵的逆存在）
print(x.dot(y)) # 单位矩阵 [[ 1.  0.][ 0.  1.]]
print(nla.det(x)) # 求行列式
