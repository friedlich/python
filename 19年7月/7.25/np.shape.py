# shape函数是numpy.core.fromnumeric中的函数，它的功能是查看矩阵或者数组的维数。

# 举例说明：
## 建立一个3×3的单位矩阵e, e.shape为（3，3），表示3行3列,第一维的长度为3，第二维的长度也为3
import numpy as np
a = np.array([[ 1.,  0.,  0.],  
              [ 0.,  1.,  0.],  
              [ 0.,  0.,  1.]])  
print(a)
print(a.shape)  

## 建立一个一维矩阵b, b.shape 为矩阵的长度
print()
b =np.array([1,2,3,4]) 
print(b)
print(b.shape)
print(np.shape([1,2,3,4]))


## 建立一个4×2的矩阵c, c.shape[1] 为第一维的长度，c.shape[0] 为第二维的长度。
print()
c = np.array([[1,1],[1,2],[1,3],[1,4]]) 
print(c)
print(c.shape)
print(c.shape[0])
print(c.shape[1])
print(c.reshape(c.shape[0],-1))
print(c.reshape(c.shape[0],-1).T)
print((c.reshape(c.shape[0],-1).T).shape)

## 一个单独的数值，返回值为空
print()
print(np.shape(3))

print()
d = np.arange(24).reshape(2,3,4)
print(d)
print(d.shape)

print()
e = np.arange(216).reshape(6,3,3,4)
print(e)
print(e.shape)
print((e.reshape(e.shape[0],-1)).shape)
print((e.reshape(e.shape[0],-1).T).shape)
print(e[:,:,:,1])
print(e[:,:,1,1])
print(e[:,1,1,1])
print(e[1,1,1,1])
print('索引一下')
index = 2
print(e[index])
print(e[2,1,1,2])

f = np.array([[1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,0,
  0,1,0,0,1,1,1,0,0,0,1,1,1,0]])
print(f)
print(f.shape)
print(f[0])
# print(f[1]) #这个立马报错，超过索引
print(f[:])
print(f[0,index])
print(f[:,index])
print(str(f[:,index]))
print(f[:,5])  # :这个东西应该是取全部的，整体的意思，具体的数字才是具体的索引，就是你最里面的一层具体的值索引出来后，
               #  外面还有一层括号在等着你，就是这个意思






