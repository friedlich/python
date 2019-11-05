# 题目 按逗号分隔列表。
# 程序分析 无。 Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。 str.join(sequence)
L = [1,2,3,4,5]
print(type(str(n) for n in L))
a = (type(str(n) for n in L))
print(a.next()) # AttributeError: type object 'generator' has no attribute 'next'
print(type([str(n) for n in L]))
print([str(n) for n in L])
print(','.join(str(n) for n in L))