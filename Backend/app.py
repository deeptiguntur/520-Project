from flask import Flask
app = Flask(__name__)
import re
from cryptography.fernet import Fernet #encrypt
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import base64


# Create a new client and connect to the server
uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Shopfinity']  # Replace
collection = db['Login_Details']  # Replace
product_collection = db['Product_Details']  # Replace
cart_collection=db['Cart_Details']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route("/")
def home():
    return "Hello, Flask!"

#encryption
# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)
def encrypt(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text
def decrypt(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text


# API endpoint for Login
@app.route("/login", methods=['POST'])
@cross_origin(origin='*')
def login():
    loginData = request.get_json()
    user=loginData['username']
    passw=loginData['password']

    #encryption
    # encrypted_username = encrypt(user)
    # encrypted_password = encrypt(passw)
    # print("encrypted_username 11 : ",encrypted_username)
    # print("encrypted_password 11 : ",encrypted_password)
    # decrypted_username = decrypt(encrypted_username)
    # decrypted_password = decrypt(encrypted_password)

    user_entry = collection.find_one({'username': user, 'password': passw})
    if user_entry:
        print("Login successful for user ")
        print(user)
        return {'res':'True', 'user_type': user_entry['user_type'], 'user_id': str(user_entry.get('_id'))}
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
    # encrypted_username = encrypt(username)
    # encrypted_password = encrypt(password)
    # Create a document to insert into MongoDB
    user_data = {
        'user_type': user_type,
        'email': email,
        'username': username,
        'first_name':first_name,
        'last_name':last_name,
        'address': address,
        'phone':phone,
        'password':password
    }
    # print("encrypted_username 2 : ",encrypted_username)
    # print("encrypted_password 2 : ",encrypted_password)

    ##Insert the document into the MongoDB collection
    result = collection.insert_one(user_data)

    if result.inserted_id:
        return {'res': 'True', 'msg': "Signup successful!"}
    else:
        return {'res': 'False', 'msg:': "Error occurred during signup"}

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

@app.route("/product/all-products", methods=['GET'])
@cross_origin(origin='*')
def getAllProducts():
    # products = product_collection.find().toArray()
    products = list(product_collection.find())
    product_list = []
    for product in products:
        product['_id'] = str(product.get('_id'))
        product_list.append(product)
    return product_list 
@app.route("/orders", methods=['GET'])
@cross_origin(origin='*')
def orderdetails():
    orders = list(cart_collection.find())
    order_list = []
    # for order in orders:
    #     order['_id'] = str(order.get('_id'))
    #     order_list.append(order)
    # return order_list 
    products = list(product_collection.find())  # Retrieve all products

    # Add image data to each order based on product_id
    for order in orders:
        for product in products:
            product['_id']=str(product.get('_id'))
            if product['_id'] == order['product_id']:
                print("Hi")
                order['_id'] = str(order.get('_id'))
                order['imgData'] = product.get('imgData')
               


                order_list.append(order)
    return order_list 
if __name__ == "__main__":
    app.run(debug=True)

    

