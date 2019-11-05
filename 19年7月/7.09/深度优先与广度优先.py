# 实现功能：深度优先遍历（只是作为某一个数据结构的一部分，并不能运行，只是演示原理）
# 采用方法：递归实现（对递归有兴趣的童鞋可以去了解下，自己实现数据结构时经常用到）
def depth_first(Root_Node):
    if Root_Node is None:
        # 递归到底的情况是：如果当前结果为None，就直接return
        return
        print(Root_Node.value)
    if Root_Node.Left_Node:
        # 如果当前节点有左子节点，那么就递归，将当前节点的左子节点作为参数传递进去
        return depth_first(Root_Node.Left_Node)
    if Root_Node.Right_Node:
        # 如果当前节点有右子节点，那么就递归，将当前节点的右子节点作为参数传递进去
        return depth_first(Root_Node.Right_Node)

# 再来看下⼴度优先如何⽤python进⾏实现：
def breadth_first(Root_Node):
    if Root_Node is None:
        # 递归到底的情况是：如果当前结果为None，就直接return
        return
    queue = []
    queue.append(Root_Node)
    # 将当前节点加入到队列中
    while queue:
        # 只要列表不为空，就一直循环
        Node = queue.pop(0)
        # 每次循环都将列表的第一个元素pop出去
        print(Node.value)
        if Root_Node.Left_Node:
            # 如果当前节点的左子节点存在，那么就添加到列表的尾部
            queue.append(Root_Node.Left_Node)
        if Root_Node.Right_Node:
            # 如果当前节点的右子节点存在，那么就添加到列表的尾部
            queue.append(Root_Node.Right_Node)
            # 好了，到这⾥，我们今天的分享就结束了，⼤家加油。

