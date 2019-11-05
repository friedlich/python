print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))
print(type('吴枫'))
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('utf-8'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))
print(type(b'\xce\xe2\xb7\xe3'))

from urllib.request import quote, unquote
print(quote('吴枫',encoding='utf-8'))
print(type(quote('吴枫')))
print(type(b'%E5%90%B4%E6%9E%AB'))
print(unquote('%E5%90%B4%E6%9E%AB'))

print('K'.encode('ASCII'))
# 你看到大写字母K被编码后还是K，但这两个K对计算机来说意义是不同的。前者是字符串，采用系统默认的Unicode编码，占两个字节。
# 后者则是bytes类型的数据，只占一个字节。这也验证我们前面所说的编码就是将str类型转换成bytes类型。

# 编码知识虽然看起来很琐碎，但它又是非常重要的，如果不能理解这些背景知识，指不定你哪天就会遇到坑，就像隐藏在丛林中的蛇，时不时地咬你一口。