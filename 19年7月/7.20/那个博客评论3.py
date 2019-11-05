import requests
session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log':'spiderman', #用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去。
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie':'1'
}
session.post(url,headers=headers,data=data)
print(type(session.cookies))
#打印cookies的类型,session.cookies就是登录的cookies
print(session.cookies)
#打印cookies

# <class 'requests.cookies.RequestsCookieJar'>
# <RequestsCookieJar[<Cookie 328dab9653f517ceea1f6dfce2255032=de9c4536a3cc4dc1cca9843080f4ffda for wordpress
# -edu-3autumn.localprod.forc.work/>, <Cookie wordpress_logged_in_9927dadafec8b913479e6af0fba5e181=spiderman
# %7C1563784696%7CXVsyIJ9d59IL8XjmSvQXHgVvu74v4u3urWLgIUi5xhH%7C6e15e5a9298063c82f6f7d4a24e6f0538ff261b42599
# 0e3fd75cbbb14cc62b03 for wordpress-edu-3autumn.localprod.forc.work/>, <Cookie wordpress_test_cookie=WP+Coo
# kie+check for wordpress-edu-3autumn.localprod.forc.work/>, <Cookie wordpress_sec_9927dadafec8b913479e6af0f
# ba5e181=spiderman%7C1563784696%7CXVsyIJ9d59IL8XjmSvQXHgVvu74v4u3urWLgIUi5xhH%7C070cb854c4c85855a63983537d2
# 782a6473785573f75b9c2e47521df93e2eb7d for wordpress-edu-3autumn.localprod.forc.work/wp-admin>, <Cookie wor
# dpress_sec_9927dadafec8b913479e6af0fba5e181=spiderman%7C1563784696%7CXVsyIJ9d59IL8XjmSvQXHgVvu74v4u3urWLgI
# Ui5xhH%7C070cb854c4c85855a63983537d2782a6473785573f75b9c2e47521df93e2eb7d for wordpress-edu-3autumn.localp
# rod.forc.work/wp-content/plugins>]>

# RequestsCookieJar是cookies对象的类，cookies本身的内容有点像一个列表，里面又有点像字典的键与值，具体的值我们看不懂，
# 也不需要弄懂。
# 那怎么把cookies存储下来？能不能用文件读写的方式，把cookies存储成txt文件？
# 可是txt文件存储的是字符串，刚刚打印出来的cookies并不是字符串。那有没有能把cookies转成字符串的方法？
# 对了，在第4关我们知道，json模块能把字典转成字符串。我们或许可以先把cookies转成字典，然后再通过json模块转成字符串。
# 这样，就能用open函数把cookies存储成txt文件。

