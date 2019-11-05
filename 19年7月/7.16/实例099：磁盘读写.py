# 题目 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 
# 输出到一个新文件C中。
# 程序分析 无。
if __name__ == '__main__':
    import sys
    fp = open(sys.path[0]+'\\'+'test1.txt')
    a = fp.read()
    fp.close()
    fp = open(sys.path[0]+'\\'+'test2.txt')
    b = fp.read()
    fp.close()
    fp = open(sys.path[0]+'\\'+'test3.txt','w')
    list = list(a+b)
    print(list)
    list.sort()
    print(list)
    s = ''.join(list)
    print(s)
    fp.write(s)
    fp = open(sys.path[0]+'\\'+'test3.txt','r')
    print(fp.read())
    fp.close()

