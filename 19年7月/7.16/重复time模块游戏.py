# print(2**32 % 100)
# print((2**32)/100)
# import random
# i = (random.randint(0,2**32)) % 100
# print(i)
# i = (random.randint(0,2**32)) % 100
# print(i)
# i = (random.randint(0,2**32)) % 100
# print(i)
# i = (random.randint(0,2**32)) % 100
# print(i)
# i = (random.randint(0,2**32)) % 100
# print(i)
# # list = [x for x in i]
# # print(max(list))
# list1 = [ i%100 for i in range(0,2**10+1)]
# # print(list1)
# print(max(list1))

if __name__ == '__main__':
    import time,random
    play_it = input('do you want to play it.(\'y\' or \'no\')')
    while play_it == 'y':
        c = input('input a caracter:\n')
        i = random.randint(0,2**32) % 100
        print('please input the number you guess:\n')
        start = time.clock()
        a = time.time()
        guess = int(input('input your gress:\n'))
        while guess != i:
            if guess > i:
                print('please input a little smaller')
                guess = int(input('input your guess:\n'))
            else:
                print('please input a little biger')
                guess = int(input('input your guess:\n'))
        end = time.clock()
        b = time.time()
        var = (end-start) / 18.2
        print(var)
        if var < 15:
            print('you are very clever')
        elif var < 25:
            print('you are normal')
        else:
            print('you are stupid')
        print('Congratulations')
        print('The number you gress is {}'.format(i))
        play_it = input('do you want to play it.')




