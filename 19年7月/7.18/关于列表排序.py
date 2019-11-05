#列表排序

#方法1 列表的sort方法,会改变原列表,方法返回值为none

list1  = [(2, 2), (3, 4), (4, 1), (1, 3)]
list2 = list1.sort(key=lambda x:x[1])
print('list1:',list1)
print('list2:',list2)

'''
================ RESULT ================
list1: [(4, 1), (2, 2), (1, 3), (3, 4)]
list2: None
>>> 
'''


#方法2 单独的sort方法,不改变原列表,方法返回一个排序后的列表

list1  = [(2, 2), (3, 4), (4, 1), (1, 3)]
list2 = sorted(list1,key = lambda x:x[1])
print('list1:',list1)
print('list2:',list2)

'''
================ RESULT ================
list1: [(2, 2), (3, 4), (4, 1), (1, 3)]
list2: [(4, 1), (2, 2), (1, 3), (3, 4)]
>>>
'''