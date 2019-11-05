## 一维数组
import numpy as np
a = np.arange(0,10,1)**2
print(a)
print(a[0],a[2],a[-1],a[-2]) # 索引从0开始，-1表示最后一个索引
print(a[2:5],a[-5:-1]) # 包括起点，不包括终点
a[-1] = 100; print(a) # 赋值
a[1:4]=100; print(a) # 批量赋值
a[:6:2] = -100; print(a) # 从开始到第6个索引，每隔一个元素（步长=2）赋值
print(a[: :-1]);print(a) # 将a逆序输出，a本身未发生改变
b = [np.sqrt(np.abs(i)) for i in a]; print(b)# 通过遍历赋值

## 多维数组
print()
a = np.arange(0,20).reshape((4,5))
# print(a, a[2,3], a[:,1], a[1:4,2], a[1:3,:])
print(a)
print(a[2,3])
print(a[:,1])
print(a[1:4,2])
print(a[1:3,:])
print(a[-1]) # 相当于a[-1,:],即索引少于轴数时，确实的索引默认为整个切片
print('在这里')

b = np.arange(0,24).reshape((2,3,4))
# print(b,b[1]) # 相当于b[1,:,:] 和b[1,...]
print(b)
print(b[1])
print('-------------------')
for row in a:
    print(row) # 遍历以第一个轴为基础

