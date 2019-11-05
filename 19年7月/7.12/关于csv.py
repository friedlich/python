# CSV (Comma Separated Values)，即逗号分隔值（也称字符分隔值，因为分隔符可以不是逗号），是一种常用的文本
# 格式，用以存储表格数据，包括数字或者字符

# reader(csvfile, dialect='excel', **fmtparams)
# writer(csvfile, dialect='excel', **fmtparams)

# csvfile，必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象，如果是文件对
# 象，打开时需要加"b"标志参数。

# dialect，编码风格，默认为excel的风格，也就是用逗号（,）分隔，dialect方式也支持自定义，通过调用register_dialect方法来注册，
# 下文会提到。
    
# fmtparam，格式化参数，用来覆盖之前dialect对象指定的编码风格。


import csv,sys 
with open(sys.path[0]+'\\shiyan.csv','rb',encoding='utf-8-sig') as myFile:  
    lines=csv.reader(myFile) 
    # print(lines.next()) 
    for line in lines:  
        print(line)  
# 'shiyan.csv'是文件名，‘rb’中的r表示“读”模式，因为是文件对象，所以加‘b’。open()返回了一个文件对象myFile，reader(myFile)
# 只传入了第一个参数，另外两个参数采用缺省值，即以excel风格读入。reader()返回一个reader对象lines,lines是一个list，当调用它
# 的方法lines.next()时，会返回一个string。上面程序的效果是将csv文件中的文本按行打印，每一行的元素都是以逗号分隔符','分隔得来。

# with open(sys.path[0]+'\\shiyan.csv','rb',encoding='utf-8-sig') as myFile:
# ValueError: binary mode doesn't take an encoding argument

# _csv.Error：迭代器应该返回字符串，而不是字节（你是否在文本模式下打开文件？）


 