from pymongo import MongoClient

client = MongoClient('localhost', 27017)
restaurants_db = client.restaurants
collection = restaurants_db.winners