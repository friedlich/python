# 忽略想起了一句台词，“有人的地方就有江湖”，那么有数组这样的数据结构一定涉及到排序，取最大值，取最小值。
import heapq
nums = [10,2,9,100,80]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
students = [{'names':'CC','scores':100,'height':189},
            {'names':'BB','scores':10,'height':169},
            {'names':'AA','scores':80,'height':179}]
print(heapq.nsmallest(2,students,key=lambda x:x['height']))
print(heapq.nlargest(2,students,key=lambda x:x['height']))
# 点评：这个heapq库非常好用，尤其是我们在取一些列表的头部数据，比如最大几个，最小几个经常用到，很实用的一招！
# 啥也不说了，赶紧背下来