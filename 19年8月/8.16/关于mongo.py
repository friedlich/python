import pymongo
client = pymongo.MongoClient('localhost')
db = client['newtestdb']
db['table'].insert({'name':'Bob'})
print(db['table'].insert({'name':'Bob'}))
db['table'].find_one({'name':'Bob'})
print(db['table'].find_one({'name':'Bob'}))