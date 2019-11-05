if __name__ == '__main__':
    while True:
        zi = int(input('请输入任一个奇数：'))
        if zi%2 !=0:
            break
    c9 = 1
    n1 = 1
    m9 = 9
    sum = 9
    while n1!=0:
        if sum % zi == 0:
            n1=0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print('{}个 9 能被 {} 整除：{}'.format(c9,zi,sum))
    r = int(sum/zi)
    print('{} / {} = {}'.format(sum,zi,r))
    
