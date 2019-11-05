# 题目 求100之内的素数。
# 程序分析 用else执行for循环的奖励代码（如果for是正常完结，非break）。
hi = int(input('请输入上限：'))
lo = int(input('请输入下限：'))
for i in range(lo,hi+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        # print(i) 这里的话其实就和前面的if,break没关系了，break只是打断for循环，for循环之后的这里会把所有的i都打出
        else:  # 这里else位置要放准了，是对于前面for循环整体下的else，而不是对于单个i%j
            print(i)
