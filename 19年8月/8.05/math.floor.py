# Math.floor() 返回小于或等于一个给定数字的最大整数
# Note:  Math.floor() === 向下取整
# 返回值: 一个表示小于或等于指定数字的最大整数的数字
# 由于 floor 是 Math 的一个静态方法，你总是应该像这样使用它 Math.floor()，
# 而不是作为你创建的一个Math对象的一种方法（Math不是一个构造函数）
import math
print(math.floor(45.95))
print(math.floor(45.05))
print(math.floor(4))
print(math.floor(-45.05))
print(math.floor(-45.95))
print(math.floor(18/4))