# 题目 输出一个随机数。
# 程序分析 使用 random 模块。 uniform() 方法将随机生成下一个实数，它在 [x, y] 范围内。
# 返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。 
import random
print(random.uniform(20,10))
print(int(random.uniform(20,10)))
 

