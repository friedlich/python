# 题目 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# 程序分析 无。i
if __name__ == '__main__':
    import sys
    fp = open(sys.path[0]+'\\'+'test2.txt','w')
    str = input('please input a string: \n')
    str = str.upper()
    fp.write(str)
    fp = open(sys.path[0]+'\\'+'test2.txt','r')
    print(fp.read())
    fp.close()


