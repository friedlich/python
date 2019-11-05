# 完整代码如下：
import requests
from bs4 import BeautifulSoup
import random
ip_list = []
def get_ip_list(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res = BeautifulSoup(res.text, 'html.parser')
    results = res.select('#ip_list tr')
    for result in results[1:]:
        ip = result.select('td')[1].text
        port = result.select('td')[2].text
        judge(ip, port)
def judge(ip, port):
    proxy = {'http': ip+':'+port}
    try:
        res = requests.get('https://www.baidu.com', proxies=proxy)
    except Exception:
        print('该ip：' + ip + '无效')
        return False
    else:
        if 200 <= res.status_code < 300: # 返回的状态码在200到300之间表示请求成功
            ip_list.append((ip, port))
            return True
        else:
            print('该ip：' + ip + '无效')
            return False
def get_random_ip():
    ip, port = random.choice(ip_list)
    result = judge(ip, port)
    if result:
        return ip + ':' + port
    else:
        ip_list.remove((ip, port))
if __name__ == '__main__':
    get_ip_list('https://www.xicidaili.com/wt/')
    print(ip_list)
    print(len(ip_list))
# 这样，我们就得到了⼀个可⽤的ip代理池，可惜，遗憾的是免费的ip代理往往不稳定，绝⼤多
# 数ip都是不可⽤的，⼤家可以去尝试下。
# 好啦，今天的讨论到这⾥就结束了，⼤家加油。