from pymongo import MongoClient

#Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["biblioteca_db"]