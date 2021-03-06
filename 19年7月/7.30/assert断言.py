# 在开发一个程序时候，与其让它运行时崩溃，不如在它出现错误条件时就崩溃（返回错误）。这时候断言assert 就显得非常有用。

# assert的语法格式：
#     assert expression
# 它的等价语句为：
    # if not expression:
    #     raise AssertionError

# 这段代码用来检测数据类型的断言，因为 a_str 是 str 类型，所以认为它是 int 类型肯定会引发错误。
a_str = 'this is a string'
print(type(a_str))
assert type(a_str)== str
# assert type(a_str)== int
