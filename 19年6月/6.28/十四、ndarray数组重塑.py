import numpy

print('ndarray数组重塑')
x = numpy.arange(0,6) #[0 1 2 3 4 5]
print(x) #[0 1 2 3 4 5]
print(x.reshape((2,3))) # [[0 1 2][3 4 5]]
print(x) #[0 1 2 3 4 5]
print(x.reshape((2,3)).reshape((3,2))) # [[0 1][2 3][4 5]]
y = numpy.array([[1,1,1],[1,1,1]])
x = x.reshape(y.shape)
print(x) # [[0 1 2][3 4 5]]
print(x.flatten()) # [0 1 2 3 4 5]
x.flatten()[0] = -1 # flatten返回的是拷贝
print(x) # [[0 1 2][3 4 5]]
print(x.ravel()) # [0 1 2 3 4 5]
x.ravel()[0] = -1 # ravel返回的是视图（引用） 
print(x) # [[-1 1 2][3 4 5]]
print("维度大小自动推导")
arr = numpy.arange(15)
print(arr.reshape((5, -1))) # 15 / 5 = 3
