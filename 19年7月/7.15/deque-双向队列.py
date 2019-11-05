# 最近在pythonTip做题的时候，遇到了deque模块，以前对其不太了解，现在特此总结一下
# deque模块是python标准库collections中的一项，它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作。
# 1.创建deque序列：
# from collections import deque
# d=deque()
# 2.deque提供了类似list的操作方法：
# d=deque()
# d.append(3)
# d.append(8)
# d.append(1)
# 那么此时d=deque([3,8,1]),len(d)=3,d[0]=3,d[-1]=1
# 3.两端都使用pop:
# d=deque(‘12345’)
# 那么d=deque(['1', '2', '3', '4', '5'])
# d.pop()抛出的是’5’,d.leftpop()抛出的是’1’，可见默认pop()抛出的是最后一个元素。
# 4.限制deque的长度
# d=deque(maxlen=20)
# for i in range(30):
#     d.append(str(i))
# 此时d的值为d=deque(['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'], maxlen=20),
# 可见当限制长度的deque增加超过限制数的项时，另一边的项会自动删除。
# 5.添加list各项到deque中：
# d=deque([1,2,3,4,5])
# d.extend([0])
# 那么此时d=deque([1,2,3,4,5,0])
# d.extendleft([6,7,8])
# 此时d=deque([8, 7, 6, 1, 2, 3, 4, 5, 0])
# 通过以上的一些操作，我们大致可以了解deque()的性质了。

# >>> d
# deque(['b', 'z', 'c', 'd'])
# >>>
# >>> d.remove("c")
# >>> d
# deque(['b', 'z', 'd'])

# >>> d
# deque(['a', 'b', 'c', 'd', 'c'])
# >>> d.reverse()
# >>> d
# deque(['c', 'd', 'c', 'b', 'a'])

# >>> d
# deque(['c', 'd', 'c', 'b', 'a'])
# >>> d.rotate(2)
# >>> d
# deque(['b', 'a', 'c', 'd', 'c'])
