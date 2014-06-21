from tinydb import TinyDB, where

db = TinyDB('.db.json')

db.insert({'id':1, 'post':'text', 'time':100})
db.insert({'id':2, 'post':'text', 'time':200})
db.insert({'id':2, 'post':'text', 'time':99})

d=db.search((where('time') >= 100))
print d
