import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.qiushibaike.com/hot/#')  #以糗事百科为例
soup = BeautifulSoup(res,'html.parser')

# 通过采用soup.select()方法，可以得到所需的内容。
# 其中关键点在于，对于所需内容的精准定位，通过（）内的语句来实现：

# 1、class 
# 对于html内的内容，可以通过class来进行定位，一般形式为：
soup.select('.class') #通过类名查找  这样可以定位到所有class内容的内容。
soup.select('.sister')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 2、id 
# id在一个html中是唯一的，因此可以通过id来找寻唯一的内容，形式为：
soup.select('#id') #通过 id 名查找
soup.select('#link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 3、标签
# 标签的话，可以直接寻找：
soup.select('a') #通过标签名查找
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.select('title') 
#[<title>The Dormouse's story</title>]
soup.select('b')
#[<b>The Dormouse's story</b>]

# 4、组合查找
# 某一类下的某个标签中的内容，采用空格隔开：
soup.select('.class a') #组合查找，二者需要用空格分开
soup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 5、直接子标签查找
soup.select("head > title") 
#[<title>The Dormouse's story</title>]

# 6、属性查找
soup.select('a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

