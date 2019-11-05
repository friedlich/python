import requests
from bs4 import BeautifulSoup

res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
res_bookstore.encoding = 'utf-8'
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_books = bs_bookstore.find('ul',class_='nav').find('ul').find_all('li')#我理解为最终是要find_all形式，是要取出多个同属性'li'的对象，这样才能用for循环来迭代
for tag_books in list_books:
    kind = tag_books.find('a')#这里面的话是要用find形式，for循环里需要是单一的对象
    kind_str = kind.text
    final = str.strip(kind_str)
    print(final)

# list_books = soup.find('u1',class_='nav')
# for tag_books in list_books:
#     kind = tag_books.find('ul').find_all('li').find('a')
#     print(kind['href'])


# [<li>
# <a href="index.html">
# <strong>Travel</strong>
# </a>
# </li>, <li>
# <a href="../mystery_3/index.html">
                            
#                                 Mystery
                            
#                         </a>
# </li>, <li>
# <a href="../historical-fiction_4/index.html">
                            
#                                 Historical Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../sequential-art_5/index.html">
                            
#                                 Sequential Art
                            
#                         </a>
# </li>, <li>
# <a href="../classics_6/index.html">
                            
#                                 Classics
                            
#                         </a>
# </li>, <li>
# <a href="../philosophy_7/index.html">
                            
#                                 Philosophy
                            
#                         </a>
# </li>, <li>
# <a href="../romance_8/index.html">
                            
#                                 Romance
                            
#                         </a>
# </li>, <li>
# <a href="../womens-fiction_9/index.html">
                            
#                                 Womens Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../fiction_10/index.html">
                            
#                                 Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../childrens_11/index.html">
                            
#                                 Childrens
                            
#                         </a>
# </li>, <li>
# <a href="../religion_12/index.html">
                            
#                                 Religion
                            
#                         </a>
# </li>, <li>
# <a href="../nonfiction_13/index.html">
                            
#                                 Nonfiction
                            
#                         </a>
# </li>, <li>
# <a href="../music_14/index.html">
                            
#                                 Music
                            
#                         </a>
# </li>, <li>
# <a href="../default_15/index.html">
                            
#                                 Default
                            
#                         </a>
# </li>, <li>
# <a href="../science-fiction_16/index.html">
                            
#                                 Science Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../sports-and-games_17/index.html">
                            
#                                 Sports and Games
                            
#                         </a>
# </li>, <li>
# <a href="../add-a-comment_18/index.html">
                            
#                                 Add a comment
                            
#                         </a>
# </li>, <li>
# <a href="../fantasy_19/index.html">
                            
#                                 Fantasy
                            
#                         </a>
# </li>, <li>
# <a href="../new-adult_20/index.html">
                            
#                                 New Adult
                            
#                         </a>
# </li>, <li>
# <a href="../young-adult_21/index.html">
                            
#                                 Young Adult
                            
#                         </a>
# </li>, <li>
# <a href="../science_22/index.html">
                            
#                                 Science
                            
#                         </a>
# </li>, <li>
# <a href="../poetry_23/index.html">
                            
#                                 Poetry
                            
#                         </a>
# </li>, <li>
# <a href="../paranormal_24/index.html">
                            
#                                 Paranormal
                            
#                         </a>
# </li>, <li>
# <a href="../art_25/index.html">
                            
#                                 Art
                            
#                         </a>
# </li>, <li>
# <a href="../psychology_26/index.html">
                            
#                                 Psychology
                            
#                         </a>
# </li>, <li>
# <a href="../autobiography_27/index.html">
                            
#                                 Autobiography
                            
#                         </a>
# </li>, <li>
# <a href="../parenting_28/index.html">
                            
#                                 Parenting
                            
#                         </a>
# </li>, <li>
# <a href="../adult-fiction_29/index.html">
                            
#                                 Adult Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../humor_30/index.html">
                            
#                                 Humor
                            
#                         </a>
# </li>, <li>
# <a href="../horror_31/index.html">
                            
#                                 Horror
                            
#                         </a>
# </li>, <li>
# <a href="../history_32/index.html">
                            
#                                 History
                            
#                         </a>
# </li>, <li>
# <a href="../food-and-drink_33/index.html">
                            
#                                 Food and Drink
                            
#                         </a>
# </li>, <li>
# <a href="../christian-fiction_34/index.html">
                            
#                                 Christian Fiction
                            
#                         </a>
# </li>, <li>
# <a href="../business_35/index.html">
                            
#                                 Business
                            
#                         </a>
# </li>, <li>
# <a href="../biography_36/index.html">
                            
#                                 Biography
                            
#                         </a>
# </li>, <li>
# <a href="../thriller_37/index.html">
                            
#                                 Thriller
                            
#                         </a>
# </li>, <li>
# <a href="../contemporary_38/index.html">
                            
#                                 Contemporary
                            
#                         </a>
# </li>, <li>
# <a href="../spirituality_39/index.html">
                            
#                                 Spirituality
                            
#                         </a>
# </li>, <li>
# <a href="../academic_40/index.html">
                            
#                                 Academic
                            
#                         </a>
# </li>, <li>
# <a href="../self-help_41/index.html">
                            
#                                 Self Help
                            
#                         </a>
# </li>, <li>
# <a href="../historical_42/index.html">
                            
#                                 Historical
                            
#                         </a>
# </li>, <li>
# <a href="../christian_43/index.html">
                            
#                                 Christian
                            
#                         </a>
# </li>, <li>
# <a href="../suspense_44/index.html">
                            
#                                 Suspense
                            
#                         </a>
# </li>, <li>
# <a href="../short-stories_45/index.html">
                            
#                                 Short Stories
                            
#                         </a>
# </li>, <li>
# <a href="../novels_46/index.html">
                            
#                                 Novels
                            
#                         </a>
# </li>, <li>
# <a href="../health_47/index.html">
                            
#                                 Health
                            
#                         </a>
# </li>, <li>
# <a href="../politics_48/index.html">
                            
#                                 Politics
                            
#                         </a>
# </li>, <li>
# <a href="../cultural_49/index.html">
                            
#                                 Cultural
                            
#                         </a>
# </li>, <li>
# <a href="../erotica_50/index.html">
                            
#                                 Erotica
                            
#                         </a>
# </li>, <li>
# <a href="../crime_51/index.html">
                            
#                                 Crime
                            
#                         </a>
# </li>]
