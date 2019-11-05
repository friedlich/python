import numpy as np

# tf.argmax(input,axis)根据axis取值的不同返回每行或者每列最大值的索引。 这个很好理解，只是tf.argmax()的参数让人有些迷惑，比如，
# tf.argmax(array, 1)和tf.argmax(array, 0)有啥区别呢？ 这里面就涉及到一个概念：axis。上面例子中的1和0就是axis。我先笼统的解释这个问题，
# 设置axis的主要原因是方便我们进行多个维度的计算。
test = np.array([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
print(test)
print(np.argmax(test, 0))
print(np.argmax(test, 1))

# axis=0时比较每一列的元素，将每一列最大元素所在的索引记录下来，最后输出每一列最大元素所在的索引数组。
# axis=1的时候，将每一行最大元素所在的索引记录下来，最后返回每一行最大元素所在的索引数组。
