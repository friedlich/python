# （1）np.linalg.inv()：矩阵求逆
# （2）np.linalg.det()：矩阵求行列式（标量）

# np.linalg.norm
# 顾名思义，linalg=linear+algebra，norm则表示范数，首先需要注意的是范数是对向量（或者矩阵）的度量，是一个标量（scalar）：

# 这里我们只对常用设置进行说明，x表示要度量的向量，ord表示范数的种类
# 参数 	说明 	计算方法
# 默认 	二范数：ℓ2  x21+x22+…+x2n−−−−−−−−−−−−−−−√	
# ord=2  二范数：ℓ2  同上
# ord=1  一范数：ℓ1  |x1|+|x2|+…+|xn|	
# ord=np.inf  无穷范数：ℓ∞  max(|xi|)
	
import numpy as np
x = np.array([3, 4])
print(np.linalg.norm(x))
print(np.linalg.norm(x))
print(np.linalg.norm(x, ord=1))
print(np.linalg.norm(x, ord=np.inf))

### 范数理论的一个小推论告诉我们：ℓ1≥ℓ2≥ℓ∞