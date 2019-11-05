# 题目 八进制转换为十进制
# 程序分析 无。
n=eval('0o'+str(int(input('八进制输入：'))))  # eval（）arg 1必须是字符串，字节或代码对象
print(n)

print(oct(int(input('请输入一个数：'))))
# print(int(input('八进制输入：')))
print(eval)
print(0o15)

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# 以下是 eval() 方法的语法:
# eval(expression[, globals[, locals]])

# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

# 返回表达式计算结果
x = 7
print(eval( '3 * x' ))
print(eval('pow(2,2)'))
print(eval('2 + 2'))
print(eval("n + 4"))
