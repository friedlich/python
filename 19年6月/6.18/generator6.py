# 小结：
# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；
# 集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可 以通过 iter() 函数获得一个 Iterator 对象。
# Python3的 for 循环本质上就是通过不断调用 next() 函数实现的，例如：

for x in [1,2,3,4,5]:
    print(x)
    break

print(next((x for x in range(1,6))))

### 对yield的总结
#   （1）通常的for..in...循环中，in后面是一个数组，这个数组就是一个可迭代
# 对象，类似的还有链表，字符串，文件。他可以是a = [1,2,3]，也可以是a = [x*x
# for x in range(3)]。
# 它的缺点也很明显，就是所有数据都在内存里面，如果有海量的数据，将会非常
# 耗内存。
#   （2）生成器是可以迭代的，但是只可以读取它一次。因为用的时候才生
# 成，比如a = (x*x for x in range(3))。!!!!注意这里是小括号而不是方括号。
#   （3）生成器（generator）能够迭代的关键是他有next()方法，工作原理就
# 是通过重复调用next()方法，直到捕获一个异常。
#   （4）带有yield的函数不再是一个普通的函数，而是一个生成器
# generator，可用于迭代
#   （5）yield是一个类似return 的关键字，迭代一次遇到yield的时候就返回
# yield后面或者右面的值。而且下一次迭代的时候，从上一次迭代遇到的yield后
# 面的代码开始执行
#   （6）yield就是return返回的一个值，并且记住这个返回的位置。下一次迭
# 代就从这个位置开始。
#   （7）带有yield的函数不仅仅是只用于for循环，而且可用于某个函数的参
# 数，只要这个函数的参数也允许迭代参数。
#   （8）send()和next()的区别就在于send可传递参数给yield表达式，这时候
# 传递的参数就会作为yield表达式的值，而yield的参数是返回给调用者的值，也
# 就是说send可以强行修改上一个yield表达式值。
#   （9）send()和next()都有返回值，他们的返回值是当前迭代遇到的yield的时
# 候，yield后面表达式的值，其实就是当前迭代yield后面的参数。
#   （10）第一次调用时候必须先next（）或send（）,否则会报错，send后之
# 所以为None是因为这时候没有上一个yield，所以也可以认为next（）等同于
# send(None)