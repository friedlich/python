def input_new(info):
    info_divided = info.split()
    print(info_divided)
    dict = {}
    key = []
    value = []
    
    
    for item in info_divided:
        if ':' in item:
            item = item[:-1]
            key.append(item)
        else:
            continue
    
    for i in range(len(key)):
        o = 2*(i+1)-1
        if ':' in info_divided[o]:
            info_divided.insert(o,'')
            value.append('')
        else:
            value.append(info_divided[o])
    print(value)
    for i in range(len(key)):
        dict[key[i]]=value[i]

    return dict

info ='''g_tk: 5381
loginUin: 0
hostUin: 0
format: json
inCharset: utf8
outCharset: GB2312
notice: 0
platform: yqq.json
needNewCode: 0
cid: 205360772
reqtype: 
biztype: 1
topid: 102065756
cmd: 8
needmusiccrit: 0
pagenum: 0
pagesize: 25
lasthotcommentid: 
domain: qq.com
ct: 24
cv: 10101010''' 
#print(info)
dict = input_new(info)
print(dict)
