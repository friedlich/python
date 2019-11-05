# 语法：numpy.squeeze(a,axis = None)
# 1）a表示输入的数组；
# 2）axis用于指定需要删除的维度，但是指定的维度必须为单维度，否则将会报错；
# 3）axis的取值可为None 或 int 或 tuple of ints, 可选。若axis为空，则删除所有单维度的条目；
# 4）返回值：数组
# 5) 不会修改原数组；

# 作用：从数组的形状中删除单维度条目，即把shape中为1的维度去掉

# 场景：在机器学习和深度学习中，通常算法的结果是可以表示向量的数组（即包含两对或以上的方括号形式[[]]），如果直接利用这个数
# 组进行画图可能显示界面为空（见后面的示例）。我们可以利用squeeze（）函数将表示向量的数组转换为秩为1的数组，这样利用
# matplotlib库函数画图时，就可以正常的显示结果了。

#例1
import numpy as np
a = np.arange(10).reshape(1,10)
print(a)
print(a.shape)
b = np.squeeze(a)
print(b)
print(b.shape)

#例2
print()
c = np.arange(10).reshape(2,5)
print(c)
print(c.shape)
print(np.squeeze(c))
print(np.squeeze(c).shape)

#例3
print()
d = np.arange(10).reshape(1,2,5)
print(d)
print(np.squeeze(d))
print(np.squeeze(d).shape)

###
# 结论：根据上述例1~3可知，np.squeeze（）函数可以删除数组形状中的单维度条目，即把shape中为1的维度去掉，
# 但是对非单维的维度不起作用。

#例4
e = np.arange(10).reshape(1,10,1)
print(e)
print(np.squeeze(e))
print(np.squeeze(e).shape)

#例5
print(np.squeeze(e,axis = 0))
print(np.squeeze(e,axis = 0).shape)

#例6
print(np.squeeze(e,axis = 2))
print(np.squeeze(e,axis = 2).shape)

#例7，指定的维度不是单维，因此会报错
# print(np.squeeze(e,axis = 1))  # ValueError: cannot select an axis to squeeze out which has size not equal to one
# ValueError：无法选择要挤出的轴，其大小不等于1

#例8：matplotlib画图示例
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
#无法正常显示图示案例
squares = np.array([[1,4,9,16,25]]) 
print(squares)
print(squares.shape)  #要显示的数组为可表示1行5列的向量的数组
# plt.plot(squares)
# plt.show()
#正常显示图示案例
#通过np.squeeze()函数转换后，要显示的数组变成了秩为1的数组，即（5，）
plt.plot(np.squeeze(squares))    
plt.show()
print(np.squeeze(squares))
print(np.squeeze(squares).shape)

#例9
import numpy as np
A = np.array([[0.6]])  #定义一个一行一列的数组
print(A)
print(A.shape)
B = np.squeeze(A)  #将数组A中维度为1的条目删除，从而变成了0维的数组，         
print(B)           #B虽然是0维，但是仍然是数组，而不是单纯的浮点数(float)
print(isinstance(B,float))  #由于B是0维数据，因此返回False
print(B.item())   #可以通过item()方法，将0维数组转换为float
print(isinstance(B.item(),float))

