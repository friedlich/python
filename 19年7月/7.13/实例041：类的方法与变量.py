# 题目 模仿静态变量的用法。
# 程序分析 构造类，了解类的方法与变量
def dummy():
    i=0 # 这里必须赋一个值啊，不然会报错，赋值前引用变量i
    print(i)
    i+=1
class cls():
    i = 0
    def dummy(self):
        print(self.i) # 对比之下类还是强的啊
        self.i += 1
a = cls()
for i in range(4):
    dummy()
    a.dummy()

