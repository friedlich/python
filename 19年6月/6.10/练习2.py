import requests

res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
pic = res.content
with open('photo.png','wb') as photo:
    photo.write(pic)
