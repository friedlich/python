# 在运行期间动态修改一个类或模块。
class A:
       def func(self):
           print("Hi")
       
def monkey():
    print("Hi, monkey")
m= A()
m.func = monkey
m.func()

