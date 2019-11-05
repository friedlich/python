# NumPy 最重要的一个对象是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，可以使用基于 0 的索引访问集合中的项目。
# ndarray 对象是用于存放同类型元素的多维数组。ndarray中的每个元素在内存中使用相同大小的块。 ndarray中的每个元素是数据类型对象的对象(称为 dtype)
# numpy.array( object ,  dtype = None , ndmin = 0 ,copy = True , order = None ,  subok = False )

import numpy

a=numpy.array([1,2,3])                #一维
b=numpy.array([[1,2,3],[4,5,6]])      #二维
c=numpy.array([1,2,3],dtype=complex)  #元素类型为复数
d=numpy.array([1,2,3],ndmin=2)        #二维
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

#ndarray.shape： 这一数组属性返回一个包含数组纬度的元组，它也可以用于调整数组大小
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)           #打印shape属性
a.shape=(3,2)            #修改shape属性
print(a)

#ndarray.ndim： 这一数组属性返回数组的维数
import numpy as np
a=np.arange(24)     #np.arange返回0-23的列表类型的数据
print(a.ndim)
b=a.reshape(2,3,4)
print(b)
print(b.ndim)

#ndarray.itemsize： 这一数组属性返回数组中每个元素的字节单位长度
import numpy as np
a=np.array([1,2,3])  #默认是四个字节
print(a)
print(a.itemsize)

