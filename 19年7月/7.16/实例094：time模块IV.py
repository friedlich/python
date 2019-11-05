# 题目 时间函数举例4。
# 程序分析 如何浪费时间。
if __name__ == '__main__':
    import time
    import random
    
    play_it = input('do you want to play it.(\'y\' or \'n\')')
    while play_it == 'y':
        c = input('input a character:\n')
        i = random.randint(0,2**32) % 100
        print ('please input number you guess:\n')
        start = time.clock()
        a = time.time()
        guess = int(input('input your guess:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little bigger')
                guess = int(input('input your guess:\n'))
        end = time.clock()
        b = time.time()
        var = (end - start) / 18.2
        print (var)
        # print('It took you {} seconds'.format(time.difftime(b,a)))
        if var < 15:
            print ('you are very clever!')
        elif var < 25:
            print ('you are normal!')
        else:
            print ('you are stupid!')
        print ('Congradulations')
        print ('The number you guess is %d' % i)
        play_it = input('do you want to play it.')


# C语言函数difftime（）
# 头文件：#include <time.h>
# 定义函数: double difftime(time_t time2, time_t time1);
# 函数说明: 返回两个time_t型变量之间的时间间隔，即 计算两个时刻之间的时间差。

# C 库函数 double difftime(time_t time1, time_t time2) 返回 time1 和 time2 之间相差的秒数 (time1 - time2)。
# 这两个时间是在日历时间中指定的，表示了自纪元 Epoch（协调世界时 UTC：1970-01-01 00:00:00）起经过的时间。
