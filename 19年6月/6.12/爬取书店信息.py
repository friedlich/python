import requests
from bs4 import BeautifulSoup

res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_books = bs_bookstore.find_all(class_='product_pod')
for tag_books in list_books:
    tag_name = tag_books.find('h3').find('a') # 找到a标签需要提取两次
    list_star = tag_books.find('p',class_="star-rating")
    # 这个p标签的class属性有两种："star-rating"，以及具体的几星比如"Two"。我们选择所有书都有的class属性："star-rating"
    tag_price = tag_books.find('p',class_="price_color") # 价格比较好找，根据属性提取，或者标签与属性一起都可以
    print(tag_name['title']) # 这里用到了tag['属性名']提取属性值
    print('star-rating:',list_star['class'][1])
    # 同样是用属性名提取属性值
    # 用list_star['class']提取出来之后是一个由两个值组成的列表，如："['star-rating', 'Two']"，我们最终要提取的是这个列表的第1个值："Two"。
    # 为什么是列表呢？因为这里的class属性有两个值。其实，在这个过程中，我们是使用class属性的第一个值提取出了第二个值。
    print('Price:',tag_price.text, end='\n'+'------'+'\n') # 打印的时候，我加上了换行，为了让数据更加清晰地分隔开，当然你也可以不加。