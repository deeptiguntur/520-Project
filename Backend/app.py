from flask import Flask
app = Flask(__name__)
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import request, jsonify
from flask_cors import CORS, cross_origin

# Create a new client and connect to the server
uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Shopfinity']  # Replace
collection = db['Login_Details']  # Replace
product_collection = db['Product_Details']  # Replace

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route("/")
def home():
    return "Hello, Flask!"
    
# API endpoint for Login
@app.route("/login", methods=['POST'])
@cross_origin(origin='*')
def login():
    loginData = request.get_json()
    user=loginData['username']
    passw=loginData['password']
    user_entry = collection.find_one({'username': user, 'password': passw})
    if user_entry:
        print("Login successful for user ")
        print(user)
        return {'res':'True'}
    else:
        print("Invalid username or password. Please try again.")
        return {'res':'False'}


#API endpoint for signup 
@app.route('/signup', methods=['POST'])
@cross_origin(origin='*')
def signup():
    signupData=request.get_json()
    # Get form data
    user_type=signupData['user_type']
    email = signupData['email']
    username = signupData['username']
    first_name=signupData['first_name']
    last_name=signupData['last_name']
    address=signupData['address']
    phone=signupData['phone']
    password = signupData['password']

    # Create a document to insert into MongoDB
    user_data = {
        'user_type': user_type,
        'email': email,
        'username': username,
        'first_name':first_name,
        'last_name':last_name,
        'address': address,
        'phone':phone,
        'password': password
    }

    ##Insert the document into the MongoDB collection
    result = collection.insert_one(user_data)

    if result.inserted_id:
        return "Signup successful! User ID: {}".format(result.inserted_id)
    else:
        return "Error occurred during signup"

# Add product to DB
@app.route("/seller/add-product", methods=['POST'])
@cross_origin(origin='*')
def addProduct():
    productData = request.get_json()
    result = product_collection.insert_one(productData)
    if result.inserted_id:
        return {
            'res': 'True',
            'msg': "Added Product!: {}".format(result.inserted_id)
        }
    else:
        return {
            'res': 'True',
            'msg': "Error occurred during adding product"
        }
    

if __name__ == "__main__":
    app.run(debug=True)

    

