## 二进制实际上就是用10进制的数的每一位数字的2的幂数
# 然后在python的操作中，只要在数字前面加上0b的字符，就可以用二进制来表示十进制数了。
print(0b1)
print(0b10)
print(0b11)
print(0b100)
print(0b101)
print(0b110)
print(0b111)
print(0b1 + 0b11)
print(0b11 * 0b11)

## 随后，在python的函数中，有一个bin()函数，直接可以将输入的十进制数，转换成二进制，但是，输出的格式是str，不是number！！
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
print(bin(9))

shift_right = 0b1100
shift_left = 0b1
shift_right = shift_right>>2
shift_left = shift_left<<2
print(bin(shift_right))
print(bin(shift_left))

# 首先来讲AND运算，什么意思呢，就是，比较2个数字，只有在这2个数字的位数上，2者都是1的情况下，才能继承1，不然则得0
# 接着我们来看下OR运算,位数中，只要有一位是1，那就继承1，两者都为0的时候才是0.
# 接着是异或运算XOR，这个是什么意思呢？就是，只有当2个运算数字的位数上，有一者为0的时候，才继承1，其余皆生成0，即使是2者都为1，也是0，两者都为0，也是0.

# 位掩码什么功能呢？他可以检测指定位数的bit是on还是off，比如他用一个0b0100的数字和一个目标数字去做AND运算，以期检测这个目标数
# 字从右往左第三位是否是on的状态，如果输出结果是大于0的，那么这个位置肯定是1.
# 还有功能就是可以翻转位数的on或者off
# 然后第三张图片，他是通过OR运算，用0去或运算目标数字的位数，来期望检测目标数位是on还是off的结果。
# 后面第四张图的异或XOR运算，也是此意。
# 第五张照片，是通过位移的方法，来翻转位数，通过左移9位，来将第10位数翻转到on.
num = 0b1100
mask = 0b0100
desired = num & mask
print(desired)
if desired > 0:
    print('Bit was on')

a = 0b110
mask = 0b1
desired = a | mask
print(desired)

a = 0b110
mask = 0b111
desired = a ^ mask
print(desired)

a = 0b101
mask = (0b1 << 9)
desired = a ^ mask
print(desired)
