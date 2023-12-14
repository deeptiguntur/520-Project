from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Shopfinity']
collection = db['Login_Details']
product_collection = db['Product_Details']
cart_collection = db['Cart_Details']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!, hey its me model working ")
except Exception as e:
    print(e)
