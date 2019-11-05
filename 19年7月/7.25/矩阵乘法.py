### Python中的几种矩阵乘法

## 1. 同线性代数中矩阵乘法的定义： np.dot()
# np.dot(A, B)：对于二维矩阵，计算真正意义上的矩阵乘积，同线性代数中矩阵乘法的定义。对于一维矩阵，计算两者的内积。
# 见如下Python代码：
import numpy as np

# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_matrix_one)
# 2-D array: 3 x 2
two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])
print(two_dim_matrix_two)

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
print('two_multi_res: %s' %(two_multi_res))

# 1-D array
one_dim_vec_one = np.array([1, 2, 3])
print(one_dim_vec_one)
one_dim_vec_two = np.array([4, 5, 6])
print(one_dim_vec_two)
one_result_res = np.dot(one_dim_vec_one, one_dim_vec_two)
print('one_result_res: %s' %(one_result_res))
print(one_dim_vec_one.dot(one_dim_vec_two))


## 2. 对应元素相乘 element-wise product: np.multiply(), 或 *
import numpy as np

print()
# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_matrix_one)
another_two_dim_matrix_one = np.array([[7, 8, 9], [4, 7, 1]])
print(another_two_dim_matrix_one)

# 对应元素相乘 element-wise product
element_wise = two_dim_matrix_one * another_two_dim_matrix_one
print('element wise product: %s' %(element_wise))

# 对应元素相乘 element-wise product
element_wise_2 = np.multiply(two_dim_matrix_one, another_two_dim_matrix_one)
print('element wise product: %s' % (element_wise_2))

