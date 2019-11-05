# 我们首先来看看namedtuple，从字面意思可以看出它和元组有关，他是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple
# 元素的个数，并可以用属性引用tuple的某个元素。同时它又具备了元组的性质。
# 如下我们使用它来定义x,y,z轴坐标
# -*- coding: UTF-8 -*
import  collections
Mytuple=collections.namedtuple('Mytuple',['x','y','z'])
mtu=Mytuple(1,2,3)
print(mtu)

# 我们运行上面的代码，输出Mytuple(x=1, y=2, z=3)，可以看出相比元组，它多了前面的几个类似key的属性，我们可以通过
# mtu.x,mtu.y,mtu.z 输出三条坐标的值，如图二第二行值就是x,y,z的值
print(mtu.x,mtu.y,mtu.z)

# 下面我们在看看deque，它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作,
# 它也是是python标准库collections中的。下面我们使用它看看
import collections
myl=collections.deque()
print(type(myl))
myl.append(1)
print(myl)
myl.extend([2,3,4])
print(myl)
myl.appendleft('x')
print(myl)
myl.pop()
print(myl)
# 可以看出它可以使用list的一些属性方法，还可以使用appendleft和popleft来从开头添加删除元素
# 观察以上deque的输出结果
# deque([1])
# deque([1, 2, 3, 4])
# deque(['x', 1, 2, 3, 4])
# deque(['x', 1, 2, 3])
# 都是deque类型，如果我们要把它转化成list,
print(list(myl))  # 就可以了



# 下面我们在看看collections的defaultdict，相比dic它可以定义一个，dic没有键的时候不报错，输出你定义的类容
import collections
mydic=collections.defaultdict(lambda :'None')
mydic['d']='ddd'
print(mydic['d'])
print(mydic['xx'])
# 输出结果：
# ddd
# None

# 我们在看看collections的OrderedDict，OrderedDict会把字典的Key按照插入的先后顺序排列
# 如下代码：
mydico=collections.OrderedDict()
mydico['s']='ss'
mydico['y']='yy'
mydico['p']='pp'
print(mydico)

# 最后我们看看collections 的Counter，从字面意思就知道他是计数的，我们可以用它统计一个元素出现的次数，
# 例如我统计一个list中各个元素个数，如下所示：
from collections import Counter
co=Counter()
la=['a','a','v','c','a','s']
for l in la:
    co[l]+=1
print(co)