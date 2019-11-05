html = '''
<div class="wrap">
  Hello,World
  <p>This is a paragraph.</p>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(type(doc))
wrap = doc('.wrap')
print(type(wrap))
print(wrap.text())
wrap.find('p').remove()
print(type(wrap))
print(wrap.text())