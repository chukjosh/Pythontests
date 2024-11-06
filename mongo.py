import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

print(mydb.list_collection_names())
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)