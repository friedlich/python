#!/usr/bin/python
# -*- coding: UTF-8 -*-
#@filename:RSmain.py
#@user: wheee/RenjiaLu
#@time:20180408
#@illustration:  reserve a seat 

import configparser
import json
import time
import random
import os,sys
import requests
from datetime import date, datetime
# reload(sys) 
sys.setdefaultencoding('utf-8')



#配置信息
# anum = int(time.mktime(time.strptime("2018-04-07 23:09:30", "%Y-%m-%d %H:%M:%S")  ))
# ymd_hms = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1523113200))

FLG_AGAIN = "AGAIN"
FLG_NEXTSEAT = "NEXTSEAT"
CONFIG_NAME = "RSconf.ini"
#section标签为：[openIdConf_2018-04-08]

RUNTIME =  int(time.mktime(time.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())) \
            +" 20:00:00", "%Y-%m-%d %H:%M:%S")  ))   #"2018-03-05 11:39:19" 
READYTIME = RUNTIME - 30 #提前 0.5 分钟准备
delayTime = 10

mheaders =  {
'Host': 'wechat.v2.traceint.com',
'User-Agent':   'Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043909 Mobile Safari/537.36 MicroMessenger/6.6.5.1280(0x26060536) NetType/WIFI Language/zh_CN',
'Accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
'Accept-Encoding':  'gzip, deflate',
'Accept-Language':  'zh-CN,en-US;q=0.8'
}
mcookies = dict(FROM_TYPE="weixin" ,wechatSESS_ID="your_sessionid",
    Hm_lvt_7ecd21a13263a714793f376c18038a87="1521332626,1521734275",
    Hm_lpvt_7ecd21a13263a714793f376c18038a87=str(int(time.time())))

#=========

#类
class GlobalValue :

    #[座位标号：坐标],不同学校的座位表不同
    R1_SEATTABLE={
    #第一自习室座位编码      252 个
     '1':'39,20','10':'37,23','100':'7,21','101':'8,21','102':'10,21','103':'10,20','104':'8,20','105':'7,20','106':'5,20','107':'7,13','108':'8,12','109':'9,11','11':'36,23','110':'10,10','111':'11,9','112':'16,6','113':'16,8','114':'16,9','115':'16,11','116':'16,12','117':'16,14','118':'17,14','119':'17,12','12':'34,23','120':'17,11','121':'17,9','122':'17,8','123':'17,6','124':'19,6','125':'19,8','126':'19,9','127':'19,11','128':'19,12','129':'19,14','13':'34,24','130':'20,14','131':'20,12','132':'20,11','133':'20,9','134':'20,8','135':'20,6','136':'22,6','137':'22,8','138':'22,9','139':'22,11','14':'36,24','140':'22,12','141':'22,14','142':'23,14','143':'23,12','144':'23,11','145':'23,9','146':'23,8','147':'23,6','148':'25,6','149':'25,8','15':'37,24','150':'25,9','151':'25,11','152':'25,12','153':'25,14','154':'26,14','155':'26,12','156':'26,11','157':'26,9','158':'26,8','16':'39,24','160':'31,20','161':'29,20','162':'28,20','163':'26,20','164':'25,20','165':'23,20','166':'22,20','167':'20,20','168':'17,20','169':'15,20','17':'39,26','170':'14,20','171':'12,20','172':'12,21','173':'14,21','174':'15,21','175':'17,21','176':'20,21','177':'22,21','178':'23,21','179':'25,21','18':'37,26','180':'26,21','181':'28,21','182':'29,21','183':'31,21','184':'31,23','185':'29,23','186':'28,23','187':'26,23','188':'25,23','189':'23,23','19':'36,26','190':'22,23','191':'20,23','192':'17,23','193':'15,23','194':'14,23','195':'12,23','196':'12,24','197':'14,24','198':'15,24','199':'17,24','2':'37,20','20':'34,26','200':'20,24','201':'22,24','202':'23,24','203':'25,24','204':'26,24','205':'28,24','206':'29,24','207':'31,24','208':'31,26','209':'29,26','21':'34,27','210':'28,26','211':'26,26','212':'25,26','213':'23,26','214':'22,26','215':'20,26','216':'17,26','217':'15,26','218':'14,26','219':'12,26','22':'36,27','220':'12,27','221':'14,27','222':'15,27','223':'17,27','224':'20,27','225':'22,27','226':'23,27','227':'25,27','228':'26,27','229':'28,27','23':'37,27','230':'29,27','231':'31,27','232':'31,29','233':'29,29','234':'28,29','235':'26,29','236':'25,29','237':'23,29','238':'22,29','239':'20,29','24':'39,27','240':'17,29','241':'15,29','242':'14,29','243':'12,29','244':'14,30','245':'15,30','246':'17,30','247':'20,30','248':'22,30','249':'23,30','25':'39,29','250':'25,30','251':'26,30','252':'28,30','253':'29,30','26':'37,29','27':'36,29','28':'34,29','29':'34,30','3':'36,20','30':'36,30','31':'37,30','32':'39,30','33':'37,37','34':'36,38','35':'35,39','36':'34,40','37':'33,41','38':'26,44','39':'26,42','4':'34,20','40':'26,41','41':'26,39','42':'25,39','43':'25,41','44':'25,42','45':'25,44','46':'23,44','47':'23,42','48':'23,41','49':'23,39','5':'34,21','50':'22,39','51':'22,41','52':'22,42','53':'22,44','54':'20,44','55':'20,42','56':'20,41','57':'20,39','58':'19,39','59':'19,41','6':'36,21','60':'19,42','61':'19,44','62':'17,44','63':'17,42','64':'17,41','65':'17,39','66':'16,39','67':'16,41','68':'16,42','69':'16,44','7':'37,21','70':'11,41','71':'10,40','72':'9,39','73':'8,38','74':'7,37','75':'5,30','76':'7,30','77':'8,30','78':'10,30','79':'10,29','8':'39,21','80':'8,29','81':'7,29','82':'5,29','83':'5,27','84':'7,27','85':'8,27','86':'10,27','87':'10,26','88':'8,26','89':'7,26','9':'39,23','90':'5,26','91':'5,24','92':'7,24','93':'8,24','94':'10,24','95':'10,23','96':'8,23','97':'7,23','98':'5,23','99':'5,21'
    }
    R2_SEATTABLE={
        #第二自习室座位编码      203  个 
        '1':'33,24','10':'29,25','100':'9,30','101':'9,31','102':'7,24','103':'7,25','104':'7,26','105':'7,27','106':'7,28','107':'7,29','108':'7,30','109':'7,31','11':'29,26','110':'4,28','111':'3,28','112':'3,26','113':'4,26','114':'4,24','115':'3,24','116':'3,22','117':'4,22','118':'4,20','119':'3,20','12':'29,27','120':'3,18','121':'4,18','122':'7,20','123':'7,19','124':'7,18','125':'7,17','126':'7,16','127':'7,15','128':'9,15','129':'9,16','13':'29,28','130':'9,17','131':'9,18','132':'9,19','133':'9,20','134':'11,20','135':'11,19','136':'11,18','137':'11,17','138':'11,16','139':'11,15','14':'29,29','140':'13,15','141':'13,16','142':'13,17','143':'13,18','144':'13,19','145':'13,20','146':'19,20','147':'19,19','148':'19,18','149':'19,17','15':'29,30','150':'19,16','151':'19,15','152':'19,14','153':'19,13','154':'19,12','155':'19,11','156':'21,11','157':'21,12','158':'21,13','159':'21,14','16':'29,31','160':'21,15','161':'21,16','162':'21,17','163':'21,18','164':'21,19','165':'21,20','166':'23,20','167':'23,19','168':'23,18','169':'23,17','17':'29,32','170':'23,16','171':'23,15','172':'23,14','173':'23,13','174':'23,12','175':'23,11','176':'25,11','177':'25,12','178':'25,13','179':'25,14','18':'29,33','180':'25,15','181':'25,16','182':'25,17','183':'25,18','184':'25,19','185':'25,20','186':'27,20','187':'27,19','188':'27,18','189':'27,17','19':'27,33','190':'27,16','191':'27,15','192':'29,15','193':'29,16','194':'29,17','195':'29,18','196':'29,19','197':'29,20','198':'31,20','199':'31,19','2':'33,25','20':'27,32','200':'33,19','201':'33,20','202':'21,24','203':'19,24','21':'27,31','22':'27,30','23':'27,29','24':'27,28','25':'27,27','26':'27,26','27':'27,25','28':'27,24','29':'25,24','3':'33,28','30':'25,25','31':'25,26','32':'25,27','33':'25,28','34':'25,29','35':'25,30','36':'25,31','37':'25,32','38':'25,34','39':'25,35','4':'33,29','40':'23,35','41':'23,34','42':'23,33','43':'23,32','44':'23,31','45':'23,30','46':'23,29','47':'23,28','48':'23,27','49':'23,26','5':'31,29','50':'23,25','51':'23,24','52':'21,25','53':'21,26','54':'21,27','55':'21,28','56':'21,29','57':'21,30','58':'21,31','59':'21,32','6':'31,28','60':'21,33','61':'21,34','62':'21,35','63':'19,35','64':'19,34','65':'19,33','66':'19,32','67':'19,31','68':'19,30','69':'19,29','7':'31,25','70':'19,28','71':'19,27','72':'19,26','73':'19,25','74':'13,24','75':'13,25','76':'13,26','77':'13,27','78':'13,28','79':'13,29','8':'31,24','80':'13,30','81':'13,31','82':'13,32','83':'13,33','84':'11,33','85':'11,32','86':'11,31','87':'11,30','88':'11,29','89':'11,28','9':'29,24','90':'11,27','91':'11,26','92':'11,25','93':'11,24','94':'9,24','95':'9,25','96':'9,26','97':'9,27','98':'9,28','99':'9,29'
    }
    #[自习室编号:服务器代号]
    DICT_ROOM_KV={"ROOM_1":"323","ROOM_2":"324"}

    def __init__(self):
        pass


#订座函数
def reserveSeatFunc(mheaders,mcookies,roomId,seatId):

    gv = GlobalValue()
    roomValue = gv.DICT_ROOM_KV["ROOM_1" if roomId == "1" else "ROOM_2" ]
    seatValue = (gv.R1_SEATTABLE if roomId == "1" else gv.R1_SEATTABLE)[seatId]

    url_zuowei ="http://wechat.v2.traceint.com/index.php/reserve/index.html?f=wechat"
    url_dixzixishi = "http://wechat.v2.traceint.com/index.php/reserve/layout/libid=%s.html&1523076408"%(roomValue)
    url_querenxuanzuo = "http://wechat.v2.traceint.com/index.php/reserve/get/libid=%s&key=%s&yzm="%(roomValue,seatValue)
    url_mingriyuyue_dixzixishi = "http://wechat.v2.traceint.com/index.php/reserve/layoutApi/action=prereserve_event&libid=%s"%(roomValue)
    url_mingriyuyue_querenxuanzuo = "http://wechat.v2.traceint.com/index.php/prereserve/save/libid=%s&key=%s&yzm="%(roomValue,seatValue)

    requests.adapters.DEFAULT_RETRIES = 5
    rs = requests.Session()
    rs.keep_alive = False
    #点击【座位】进入首页
    try:
        #当日即时预定
        respone=rs.get(url_zuowei,timeout=1,headers=mheaders,cookies=mcookies)
        #明日预约
        #respone=rs.get(url_mingriyuyue_dixzixishi,timeout=1,headers=mheaders,cookies=mcookies)
    except Exception as e:
        print(u"[E]: 进入自习室出错 %s"%repr(e))
        #return ""
    else:
        if (respone.status_code == 200 ) and ((respone.text.find("出入口")>0 or (respone.text.find("自习室")))):
            print(u"[I]: 进入自习室成功-状态码：%5d"% respone.status_code+"\n")
        else:
            print(u"[I]: 进入自习室失败-状态码：%5d"% respone.status_code+"\n")
    #print(respone.content)

    #选择自习室

    #点击【确认选座】确认选座
    try:
        #当日即时预定
        respone=rs.get(url_querenxuanzuo,timeout=1,headers=mheaders,cookies=mcookies)
        #明日预约
        #respone=rs.get(url_mingriyuyue_querenxuanzuo,timeout=1,headers=mheaders,cookies=mcookies)
    except Exception as e:
        print(u"[E]: 确认选座出错 %s"%repr(e))
    else:
        #是预定成功 而不是 预订成功
        if (respone.status_code == 200) and ((respone.text.find("预定成功") > 0) or (respone.text.find("预定座位成功")>0)) :
            print(u"[I]: 第 %s 自习室 %s 号位置抢座成功!-状态码：%5d"% (roomId,seatId,respone.status_code)+"\n")
        else:
            if respone.text.find(u"已经预定") > 0:
                print(u"[I]: 第 %s 自习室 %s 号位置抢座失败!你已经预定了其他座位!-状态码：%5d"% (roomId,seatId,respone.status_code)+"\n")
            elif respone.text.find("被人预定") > 0:
                print(u"[I]: 第 %s 自习室 %s 号位置抢座失败!该座位已经被人预定了!-状态码：%5d"% (roomId,seatId,respone.status_code)+"\n")
            else:
                print(u"[I]: 第 %s 自习室 %s 号位置抢座失败!未知原因-状态码：%5d"% (roomId,seatId,respone.status_code)+"\n")
                print(respone.text)
                print(respone.url)
            return FLG_NEXTSEAT #继续抢下一个座位
    return ""

#判断当前时间处于的阶段 READY/RUN ,修改delay时长
def howAboutNow():
    global delayTime,RUNTIME,READYTIME
    ticks = int(time.time())

    if ticks >= RUNTIME :
        return "T_RUN"
    elif ticks >= READYTIME :
        delayTime = 0.2 if RUNTIME - ticks < 15  else  8
        return "T_READY"
    else :
        howlong = RUNTIME - ticks
        if howlong < 7200 :
            delayTime = 0.2 if howlong < 15  else ( 10 if howlong < 300  else ( 200 if howlong < 3600 else 2400))
        else :
            delayTime = 7200 if howlong > 10800 else 4800

        print(u"[I]: 当前时间 %s ,  %s 分钟后进入准备阶段"%\
            (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ticks)),str((READYTIME-ticks)/60)))
        return ""
#开始
if __name__ == '__main__':

    print(u"[I]: 图书馆抢座助手已启动...\n")
    todaySection = "openIdConf_%s"%time.strftime('%Y-%m-%d',time.localtime(time.time()))

    dict_openID_SESSID = {}
    isFirstReady = 1 # 1 是第一次准备，2 不是第一次则不再准备
    while True :

        nowflg = howAboutNow() 
        if "T_READY" == nowflg:
            if isFirstReady != 1 :
                continue
            print(u"[I]: 开始准备")
            try:
                #准备时间-读取配置文件
                conf = configparser.ConfigParser()
                conf.read(CONFIG_NAME)       # 文件路径
                list_tmp = conf.items(todaySection)# 返回openId_wechatSESS_ID标签项下面的键值对 list
                dict_openID_SESSID = dict(list_tmp)#openid = qlsqge7nr1m92npjcngukeghf5 , 1,23,2,188,1,187

                isFirstReady = 2 #不再是第一次准备
            except Exception as e:
                print(u"[E]: 读取配置文件出错 %s"%repr(e))

        #到达预定时间-开始抢座
        elif "T_RUN" == nowflg :
            print(u"[I]: 开始抢座 ")
            for v in dict_openID_SESSID.values():
                try:
                    listv = v.split(",")
                    mylen = len(listv)
                    mcookies["wechatSESS_ID"] = listv[0].strip()

                    returnValue = FLG_NEXTSEAT
                    key_i = 1
                    value_i = key_i + 1
                    #限制每个人备选抢座号的数量 2个
                    mylen = 5 if mylen >= 5 else mylen
                    while value_i < mylen and returnValue == FLG_NEXTSEAT:
                        t_roomid = listv[key_i].strip()
                        t_seatid = listv[value_i].strip()
                        key_i = key_i + 2
                        value_i = key_i + 1

                        #抢座！！！
                        returnValue = reserveSeatFunc(mheaders,mcookies,t_roomid,t_seatid)

                except Exception as e:
                    print(u"[E]: 抢座出错 %s"%repr(e))
            #只运行一次 抢座模块 
            break

        else :
            print(u"[I]: %s 秒后继续监听..."%delayTime)
            time.sleep(delayTime)
