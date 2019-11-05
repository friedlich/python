# 题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# 程序分析 递归真是蠢方法。
def rec(string):
    if len(string)!=1:
        rec(string[1:])
        # print(string[0],end='') 这个会少打一个最后那个字母
    print(string[0],end='')

rec(input('string here:'))

def test(n):
    if n!=1:
        test(n-1) #test(n–1)下有两个print都被隐藏，递归一结束马上反着由后往前打出来 li yang，这是先后顺序的关系
        print('li')
    print('yang')
print(test(1)) 
test(3) #不把函数print出来就没有None了，函数的返回值是None


