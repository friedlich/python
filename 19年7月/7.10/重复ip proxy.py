import requests,bs4,random,csv

def get_ip_list(url):
    res = requests.get(url,headers=headers)
    bs = bs4.BeautifulSoup(res.text,'html.parser')
    results = bs.find(id="ip_list").find_all('tr')
    for result in results[1:]:
        ip = result.find_all('td')[1].text
        port = result.find_all('td')[2].text
        judge(ip,port)

def judge(ip,port):
    proxy = {'http': ip+':'+port}
    try:
        res = requests.get('https://www.baidu.com',headers=headers,proxies=proxy)
    except Exception:
        print('该ip:' + ip + '无效')
        return False
    else:
        if 200 <= res.status_code <= 300:
            ip_list.append((ip,port))
            return True
        else:
            print('该ip:' + ip + '无效')
            return False

def get_random_ip():
    ip,port = random.choice(ip_list)
    result = judge(ip,port)
    if result:
        return ip + ':' + port
    else:
        ip_list.remove((ip,port))

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    ip_list = []
    get_ip_list('https://www.xicidaili.com/wt/1')
    # print(ip_list)
    print(len(ip_list))
    choice_ip = get_random_ip()
    print(choice_ip)
    with open(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.11\proxy.csv','w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for i in ip_list:
            writer.writerow(i)
