from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#connecting to mongodb 
uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
#connecting to database name shopfinity
db = client['Shopfinity']
#connecting to the collections(tables)
#login table
collection = db['Login_Details']
#product table
product_collection = db['Product_Details']
#cart tabe
cart_collection = db['Cart_Details']
#checking if it is working or not correctly
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!, hey its me model working ")
except Exception as e:
    print(e)
