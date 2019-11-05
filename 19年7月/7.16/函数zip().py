# Python新手可能对这个函数不是很熟悉，zip()可以返回元组的迭代器。
print(list(zip(['a','b','c'],[1,2,3])))
# 在这里zip()函数对两个列表中的数据项进行了配对，并用它们创建了元组
gene = zip(['a','b','c'],[1,2,3])
print(gene)
print(next(gene))
print(next(gene))

