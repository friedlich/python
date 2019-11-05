# 题目 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 程序分析 无。
import collections
li = [1,2,3,4,5,6,7,8,9] 
deq = collections.deque(li,maxlen=len(li))
print(li)
print(deq)
print(type(deq))
deq.rotate(int(input('rotate: ')))  # rotate（把右边元素放在左边）
print(list(deq))