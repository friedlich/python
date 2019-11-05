import redis
r = redis.Redis('localhost',6379)
print(r.set('name','Bob'))
print(r.get('name'))