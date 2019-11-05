#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/10  
# @Author  : 圈圈烃
# @File    : reservation_4.py  

import requests
import re
import json
import datetime
import time


def get_cookies():
    """获得cookies"""
    get_cookies_url = 'http://**************'
    s = requests.session()
    s.get(get_cookies_url)
    ck_dict = requests.utils.dict_from_cookiejar(s.cookies)     # 将jar格式转化为dict
    ck = 'JSESSIONID=' + ck_dict['JSESSIONID']                  # 重组cookies

    """获得二维码"""
    path = './code.png'
    get_img_headers = {
        'user-anget': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Cookie': ck}
    get_img_url = 'http://**************'
    code_image = requests.get(get_img_url , headers=get_img_headers)
    with open(path, 'wb') as fn:
        fn.write(code_image.content)
        fn.close()
        print('验证码保存成功')
    return ck


def login(cookies, hour, minute):
    login_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '45',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Host': '**************',
        'Pragma': 'no-cache',
        'Referer': 'http://**************',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    login_url = 'http://**************'
    login_data = {
        'codeImage': input('请输入验证码：'),
        'uname': '**************',
        'upass': '**************'
    }
    requests.post(login_url, data=login_data, headers=login_headers)

    res = requests.get('http://**************', headers=login_headers)
    reg_h = r'<option value=(.*?)>\d{4}-\d{2}-\d{2}'  # 匹配可提供预约的hash
    value_h = re.findall(reg_h, res.text)

    """定时"""
    counter = 0
    while (True):
        now = datetime.datetime.now()  # 获取当前系统时间
        if now.hour == hour and now.minute == minute:
            break
        time.sleep(0.5)
        # print(now)
        counter = counter + 1
        if counter == 240:
            res = requests.get('http://**************', headers=login_headers)
            reg_h = r'<option value=(.*?)>\d{4}-\d{2}-\d{2}'  # 匹配可提供预约的hash
            reg_t = r'(\d{4}-\d{2}-\d{2})'  # 匹配可提供预约的日期
            value_h = re.findall(reg_h, res.text)
            value_t = re.findall(reg_t, res.text)
            with open('./con_log.txt', 'a') as fjs:
                fjs.write(eval(value_h[-1])+'  '+value_t[-1]+'  '+str(now)+'  \n')
                fjs.close()
                print('保存成功')
            counter = 0

    return str(eval(value_h[-1]))


def reservation(day_hash, cookies, stime, etime):
    reservation_data = {
        '_etime': etime,  # 结束时间11点，其值为11*60=660
        '_roomid': '1285b3ca77594b3095c7b89d4922553c',  # 房间Id
        '_seatno': '',
        '_stime': stime,    # 开始时间8点，其值为8*60=480
        '_subject': '学习',  # 研讨主题
        '_summary': '学习',  # 研讨大纲
        'ruleId': day_hash,
        'usercount': 3,     # 预约人数
        'users': '**************',  # 学号
        'UUID': '**************'
    }

    reservation_headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '239',
        'Content-Type': 'application/json',
        'Cookie': cookies,
        'Host': '**************',
        'Pragma': 'no-cache',
        'Referer': 'http://**************',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    reservation_js = json.dumps(reservation_data)
    reservation_url = 'http://**************'
    status = requests.post(reservation_url, data=reservation_js, headers=reservation_headers)
    # print(stime, etime)
    # print(status)
    print(status.text)


def main():
    """预约策略一：11：20-20.40"""
    full_stime = ['1060', '870', '680']
    full_etime = ['1240', '1050', '860']
    """预约策略二：10：00-13：00；13：50-16：50；17：40-20:40"""
    stime = ['1060', '830', '600']
    etime = ['1240', '1010', '780']
    cookies = get_cookies()
    day_hash = login(cookies, 0, 0)     # 设定定时时间
    for i in range(0, 3):
        reservation(day_hash, cookies, stime[i], etime[i])


if __name__ == '__main__':
    main()

