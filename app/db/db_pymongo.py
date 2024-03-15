import pymongo as pyM
from bson import ObjectId
from decouple import config

client = pyM.MongoClient(config("DATABASE_URL"))

db = client.clent_test

collection = db.test_collection


print(ObjectId)
# print(db.list_collection_names())
