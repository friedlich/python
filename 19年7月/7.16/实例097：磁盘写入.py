# 题目 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# 程序分析 无。
if __name__ == '__main__':
    import sys
    from sys import stdout
    filename = input('请输入文件名：\n')
    fp = open(sys.path[0] + '\\' + filename,'w')
    str = input('请输入字符串：\n')
    while str != '#':
        fp.write(str)
        stdout.write(str+'\n')
        str = input('') # 上面不加那个'\n'换行的话，这两行就输出在一行了
    fp.close()


# import sys
# sys.stdout.write("字符串")
# sys.stdout.write在标准输出上输出字符串，与print语句的作用相似在屏幕上打印字符串 

# sys.stdout 是标准输出文件。write就是往这个文件写数据。
# 合起来就是打印数据到标准输出。
# 对初学者来说，和print功能一样。 
# 补充一下，sys.stdout.write()除了输出参数，还会额外输出参数的字符数。 

