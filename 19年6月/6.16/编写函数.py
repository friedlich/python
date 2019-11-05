# 编写函数：可以接受任何数目的参数，并判断第一个参数是否等于其余参数的和

def ssum(*numbers):
    nlist =list(numbers)
    fnum = nlist.pop(0)
    if fnum == sum(nlist):
        print('第一个数与其余数之和相等！')
        return True
    else:
        print('第一个数与其余数之和不相等！')
        return False

ssum(5,3,1,2)
ssum(5,3,1,1)