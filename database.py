from pymongo import MongoClient

# Reemplaza <usuario>, <password>, <cluster> por tus datos
MONGO_URI = "mongodb+srv://20RSebas:aerials2002@mongo-db-cluster.fqjwm4d.mongodb.net/?appName=mongo-db-cluster"

client = MongoClient(MONGO_URI)
db = client.casa_cambios
transactions_collection = db.transactions
