# 排序和查询都是好基友，长的数据结构里面(字典，列表)里面我们一定会有查询，过滤的需求。
# 有的时候，我们需要从一个很长的列表里面，找到某一个或者某一类的元素，怎么办，很简单，用高级函数filter :
# 1).用lambda配合filter过滤

# 点评:lambda是一个非常简洁的函数表达方式，短小精悍，加上配合filter一起使用，非常漂亮。比如我们通过字符串里的startswith
# 内置函数，非常方便的过滤出列表里面我们需要的数据！(Python3稍微改一下再filter之外再加一个list,不然生成的是迭代器地址)


# 或者用正则过滤
import re
list1 = ['3','b','(to_)']
print(filter(lambda x:re.findall(u'(to_)',x),list1))
print(list(filter(lambda x:re.findall(u'(to_)',x),list1)))
# 如果列表里面是一个个字典
list2 = [{'aa':100,'bb':200},{'a1':300,'dd':400}]
print(filter(lambda x :'aa' in x.keys(),list2)) # lambda函数我理解为其自身就是要规则参数满足某种条件
print(list(filter(lambda x :'aa' in x.keys(),list2)))
# 点评：正则是一个非常不错的过滤方法，有的时候好的正则顶的上几十行代码，精通正则对玩数据分析，数据清洗是必需的技能！