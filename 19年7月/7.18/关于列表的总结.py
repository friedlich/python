# a = [1,2,3,4,5,6]
# print(a[:])
# print(a[::-1])
# print(a[:5])
# print(a[3::-2])
# print(a[::-2])

###
# 对应操作：
# 1 查（［］）
names_class2=['张三','李四','王五','赵六'] 
print(names_class2[2]) 
print(names_class2[0:3]) 
print(names_class2[0:7]) 
print(names_class2[-1]) 
print(names_class2[2:3]) 
print(names_class2[0:3:1]) 
print(names_class2[3:0:-1]) 
print(names_class2[:])

# 2 增（append，insert）
# insert 方法用于将对象插入到列表中，而append方法则用于在列表末尾追加新的对象
names_class2.append('alex') 
names_class2.insert(2,'alvin') 
print(names_class2) 

# 3 改（重新赋值）
names_class2=['张三','李四','王五','赵六']   
names_class2[3]='赵七'
names_class2[0:2]=['wusir','alvin'] 
print(names_class2)

# 4 删（remove，del，pop）
names_class2=['张三', '李四', 'alvin', '王五', '赵六', 'alex']
names_class2.remove('alex') 
print(names_class2)
names_class2.pop()#注意,pop是有一个返回值的　
print(names_class2)
del(names_class2[0])
print(names_class2)

# 5 其他操作
# 5.1  count
# count 方法统计某个元素在列表中出现的次数：
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
x = [[1,2], 1, 1, [2, 1, [1, 2]]]   
print(x.count(1))   
print(x.count([1,2]))

# 5.2 extend
# extend 方法可以在列表的末尾一次性追加另一个序列中的多个值。
a = [1, 2, 3]   
b = [4, 5, 6]   
a.extend(b)   
print(a) 
# extend 方法修改了被扩展的列表，而原始的连接操作（+）则不然，它会返回一个全新的列表。
a = [1, 2, 3]   
b = [4, 5, 6]   
print(a.extend(b))  
print(a)
[1, 2, 3, 4, 5, 6]    
print(a + b)
[1, 2, 3, 4, 5, 6, 4, 5, 6]   
print(a)  
[1, 2, 3, 4, 5, 6]
# 5.3  index
# index 方法用于从列表中找出某个值第一个匹配项的索引位置：
print(names_class2.index('李四') ) 
# 5.4  reverse
# reverse 方法将列表中的元素反向存放。
names_class2.reverse() 
print(names_class2) 
# 5.5  sort
# sort 方法用于在原位置对列表进行排序。
x = [4, 6, 2, 1, 7, 9] 
x.sort()#x.sort(reverse=True) 
print(x)
x.sort(reverse=True)
print(x)
# 5.6  深浅拷贝
# 现在，大家先不要理会什么是深浅拷贝，听我说，对于一个列表，我想复制一份怎么办呢？
# 肯定会有同学说，重新赋值呗：
names_class1=['张三','李四','王五','赵六'] 
names_class1_copy=['张三','李四','王五','赵六'] 
# 这是两块独立的内存空间
# 这也没问题，还是那句话，如果列表内容做够大，你真的可以要每一个元素都重新写一遍吗？当然不啦，所以列表里为我们内置了copy方法：
names_class1=['张三','李四','王五','赵六',[1,2,3]] 
names_class1_copy=names_class1.copy() 
  
names_class1[0]='zhangsan'
print(names_class1) 
print(names_class1_copy) 
  
############ 
names_class1[4][2]=5
print(names_class1) 
print(names_class1_copy) 
  
#问题来了,为什么names_class1_copy,从这一点我们可以断定,这两个变量并不是完全独立的,那他们的关系是什么呢?为什么有的改变,
#有的不改变呢?
###
# 这里就涉及到我们要讲的深浅拷贝了：
#不可变数据类型:数字,字符串,元组         可变类型:列表,字典 
  
# l=[2,2,3] 
# print(id(l)) 
# l[0]=5 
# print(id(l))   # 当你对可变类型进行修改时,比如这个列表对象l,它的内存地址不会变化,注意是这个列表对象l,不是它里面的元素 
#                # this is the most important 
# 
# s='alex' 
# print(id(s))   #像字符串,列表,数字这些不可变数据类型,,是不能修改的,比如我想要一个'Alex'的字符串,只能重新创建一个'Alex'的对象
# ,然后让指针只想这个新对象 
# 
# s[0]='e'       #报错 
# print(id(s)) 
  
#重点:浅拷贝 
a=[[1,2],3,4] 
b=a[:]#b=a.copy() 
  
print(a,b) 
print(id(a),id(b)) 
print('*************') 
print('a[0]:',id(a[0]),'b[0]:',id(b[0])) 
print('a[0][0]:',id(a[0][0]),'b[0][0]:',id(b[0][0])) 
print('a[0][1]:',id(a[0][1]),'b[0][1]:',id(b[0][1])) 
print('a[1]:',id(a[1]),'b[1]:',id(b[1])) 
print('a[2]:',id(a[2]),'b[2]:',id(b[2])) 
  
  
print('___________________________________________') 
b[0][0]=8
  
print(a,b) 
print(id(a),id(b)) 
print('*************') 
print('a[0]:',id(a[0]),'b[0]:',id(b[0])) 
print('a[0][0]:',id(a[0][0]),'b[0][0]:',id(b[0][0])) 
print('a[0][1]:',id(a[0][1]),'b[0][1]:',id(b[0][1])) 
print('a[1]:',id(a[1]),'b[1]:',id(b[1])) 
print('a[2]:',id(a[2]),'b[2]:',id(b[2]))# <BR><BR><BR>#outcome



