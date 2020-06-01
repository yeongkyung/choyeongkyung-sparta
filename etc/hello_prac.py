from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

movie = db.movies_prac.find_one({'title':'매트릭스'})
samemovies = list(db.movies_prac.find({'star':movie['star']}))

for movie in samemovies:
    print (movie['title'])