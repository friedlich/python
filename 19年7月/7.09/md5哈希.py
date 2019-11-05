# 第三种：URL经过md5等方法哈希之后保存到set中（Scrapy框架采取的URL去重方法就是
# 类似这种方法）
# 优点：效率很高，查询快
# 缺点：耗内存（但相对第二种方法，已经缩小了几倍的内存）
# 举例：md5编码能够将一个字符缩减到固定的长度，md5的一般编码长度是128bit，那么
# 就是16byte，还是按照1亿个URL计算，需要耗费多大的内存来保存这些URL呢？
# 100000000 * 16 byte / 1024 / 1024 / 1024 ≈ 1.5G

# 实现功能：将URL通过md5哈希之后，得到一个固定长度的字符串
import hashlib
def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
        print(len(url))
        m = hashlib.md5(url)
        return(m.digest(),m.hexdigest())
        # hash.digest() 
        # 返回摘要，作为二进制数据字符串值
        # hash.hexdigest() 
        # 返回摘要，作为十六进制数据字符串值

result = get_md5('https://www.baidu.com')
print(result[0])
print(len(result[0]))
print(result[1])
print(len(result[1]))

# 第四种：用bitmap方法，将访问过的URL通过hash函数映射到某一位上，也就是某一个bit上
# 优点：进一步压缩了保存URL需耗费的内存
# 缺点：哈希冲突很高，不太适用
# 举例：一个byte有8个bit，也就是8个位，bitmap就是将一个URL通过hash函数，将它映射到8个位上的某一个位上，这样就进一步压缩了
# 保存URL需耗费的内存，但极有可能将多个URL映射到了同一个位上，也就造成了哈希冲突，造成哈希冲突后，就需要向下寻址，有兴趣的
# 童鞋可以网上搜索哈希冲突的解决方法。


# 第五种：bloomfilter方法对bitmap进行改进，多重hash函数降低哈希冲突
# 优点：既保留了bitmap的内存压缩优点，又良好解决了哈希冲突
# 缺点：难以理解
# 举例：还是按照1亿个URL来计算，采用这种方法需要占用多大的内存呢？
# 100000000 * 1 bit / 8 / 1024 / 1024/ 1024  ≈ 12M
# 当然这只是理想状况，尽管bloomfilter对bitmap进行了优化，但不可避免地还是会有哈希冲突的发生，导致内存是12M只是一种理想状况
# 下的数字，实际上肯定不止12M，但无论如何，和之前的几种方法比较，内存还是成倍地进行了压缩