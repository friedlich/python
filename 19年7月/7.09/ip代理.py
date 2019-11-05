import requests
# 免费代理可以从https://www.xicidaili. com/中获取到，但是免费的ip代理存活率很低
proxy = {
'http': '183.148.158.64:9999'
}
res = requests.get('https://www.baidu.com', proxies=proxy)
# print( res.text)
# 如果能正确返回结果，那么就说明当前ip代理是存活的，是可以用的，否则当前ip代理是失效的
## 仅仅有⼀个代理ip是不够的，我们应该维护⼀个属于⾃⼰的ip代理池，当某⼀个ip代理失效的
## 时候，就将它剔除出去，那么如何维护⼀个可⽤的ip代理池呢？
# 第一步：通过https://www.xicidaili.com/wt/获取到ip_list
import requests
from bs4 import BeautifulSoup
import random,csv

def get_ip_list(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res = BeautifulSoup(res. text, 'html.parser')
    results = res.select('#ip_list tr')
    for result in results[1:]:
        ip = result.select('td')[1].text
        port = result.select('td')[2].text
        judge(ip, port)

# 第二步：判断获取到的ip是否有效
ip_list = []
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

# 第三步：从ip_list中随机获取一个ip
def get_random_ip():
    ip, port = random.choice(ip_list)
    result = judge(ip, port)
    if result:
        return ip + ':' + port
    else:
        ip_list.remove((ip, port))

# 第四步：调用上述函数
if __name__ == '__main__':
    get_ip_list('https://www.xicidaili.com/wt/2')
    # print(ip_list)
    print(len(ip_list))  
    ip = get_random_ip() #这里终端会出现101个ip，因为这一步相当于又是调用了一次judge函数，列表等于说是在末尾加了一个重复的ip
    print(ip)  
    with open(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.10\proxy.csv','w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for i in ip_list:
            writer.writerow(i)
    





    



    

