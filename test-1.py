import pymongo
client = pymongo.MongoClient("mongodb+srv://vishwanathpatil9868:k1uI1B3l05zN8zfU@no-sql.6x0eugk.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)


d = {
    "name": "vishwanath",
    "email": "vishwanathpatil2gmail.com",
   "surname" : "patil"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )



