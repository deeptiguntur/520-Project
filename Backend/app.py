# from flask import Flask
# app = Flask(__name__)
# import re
# from cryptography.fernet import Fernet #encrypt
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# from flask import request, jsonify
# from flask_cors import CORS, cross_origin
# import base64


# # Create a new client and connect to the server
# uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client['Shopfinity']  # Replace
# collection = db['Login_Details']  # Replace
# product_collection = db['Product_Details']  # Replace
# cart_collection=db['Cart_Details']

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# #encryption
# # Generate a key for encryption and decryption
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# def encrypt(text):
#     encrypted_text = cipher_suite.encrypt(text.encode())
#     return encrypted_text
# def decrypt(encrypted_text):
#     decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
#     return decrypted_text


# # API endpoint for Login
# @app.route("/login", methods=['POST'])
# @cross_origin(origin='*')
# def login():
#     loginData = request.get_json()
#     user=loginData['username']
#     passw=loginData['password']

#     #encryption
#     # encrypted_username = encrypt(user)
#     # encrypted_password = encrypt(passw)
#     # print("encrypted_username 11 : ",encrypted_username)
#     # print("encrypted_password 11 : ",encrypted_password)
#     # decrypted_username = decrypt(encrypted_username)
#     # decrypted_password = decrypt(encrypted_password)

#     user_entry = collection.find_one({'username': user, 'password': passw})
#     if user_entry:
#         print("Login successful for user ")
#         print(user)
#         return {'res':'True', 'user_type': user_entry['user_type'], 'user_id': str(user_entry.get('_id'))}
#     else:
#         print("Invalid username or password. Please try again.")
#         return {'res':'False'}


# #API endpoint for signup 
# @app.route('/signup', methods=['POST'])
# @cross_origin(origin='*')
# def signup():
#     signupData=request.get_json()
#     # Get form data
#     user_type=signupData['user_type']
#     email = signupData['email']
#     username = signupData['username']
#     first_name=signupData['first_name']
#     last_name=signupData['last_name']
#     address=signupData['address']
#     phone=signupData['phone']
#     password = signupData['password']
#     # encrypted_username = encrypt(username)
#     # encrypted_password = encrypt(password)
#     # Create a document to insert into MongoDB
#     user_data = {
#         'user_type': user_type,
#         'email': email,
#         'username': username,
#         'first_name':first_name,
#         'last_name':last_name,
#         'address': address,
#         'phone':phone,
#         'password':password
#     }
#     # print("encrypted_username 2 : ",encrypted_username)
#     # print("encrypted_password 2 : ",encrypted_password)

#     ##Insert the document into the MongoDB collection
#     result = collection.insert_one(user_data)

#     if result.inserted_id:
#         return {'res': 'True', 'msg': "Signup successful!"}
#     else:
#         return {'res': 'False', 'msg:': "Error occurred during signup"}

# # Add product to DB
# @app.route("/seller/add-product", methods=['POST'])
# @cross_origin(origin='*')
# def addProduct():
#     productData = request.get_json()
#     result = product_collection.insert_one(productData)
#     if result.inserted_id:
#         return {
#             'res': 'True',
#             'msg': "Added Product!: {}".format(result.inserted_id)
#         }
#     else:
#         return {
#             'res': 'False',
#             'msg': "Error occurred during adding product"
#         }
# # Added selected products to cart
# #API endpoint for signup 
# @app.route('/cart', methods=['POST'])
# @cross_origin(origin='*')
# def product_cart():
#     cart_data=request.get_json()
   
#     product_id=cart_data['_id']
#     quantity = cart_data['quantity']
#     cart_insert = {
#         'product_id': product_id,
#         'quantity': quantity,
#     }
#     ##Insert the document into the MongoDB collection
#     cart_result = cart_collection.insert_one(cart_insert)

#     if cart_result.inserted_id:
#         return {
#             'res': 'True',
#             'msg': "Added Product in Cart: {}".format(cart_result.inserted_id)
#         }
#     else:
#         return {
#             'res': 'False',
#             'msg': "Error occurred while adding product in cart"
#         }

# @app.route("/product/all-products", methods=['GET'])
# @cross_origin(origin='*')
# def getAllProducts():
#     # products = product_collection.find().toArray()
#     products = list(product_collection.find())
#     product_list = []
#     for product in products:
#         product['_id'] = str(product.get('_id'))
#         product_list.append(product)
#     return product_list 
# # listing those which has products categories 
# @app.route("/category", methods=['GET'])
# @cross_origin(origin='*')
# def categorypage():
#     products = list(product_collection.find())
#     list_category = []
#     for product in products:
#         product['_id'] = str(product.get('_id'))
#         list_category.append(product)
#     return list_category 
# @app.route("/orders", methods=['GET'])
# @cross_origin(origin='*')
# def orderdetails():
#     orders = list(cart_collection.find())
#     order_list = []
#     # for order in orders:
#     #     order['_id'] = str(order.get('_id'))
#     #     order_list.append(order)
#     # return order_list 
#     products = list(product_collection.find())  # Retrieve all products

#     # Add image data to each order based on product_id
#     print(orders)
#     for order in orders:
#         for product in products:
#             product['_id']=str(product.get('_id'))
#             if product['_id'] == order['product_id']:
#                 print("Hi")
#                 order['_id'] = str(order.get('_id'))
#                 order['imgData'] = product.get('imgData')
#                 order['brand'] = product.get('brand')
#                 order['productDesc']=product.get('productDesc')
#                 order['price']=product.get('price')
#                 order['discount']=product.get('discount')

               


#                 order_list.append(order)
#     return order_list 

# #ediing product
# @app.route("/editproduct", methods=['POST'])
# @cross_origin(origin='*')
# def editProduct():
#     productData = request.get_json()
#     product_id = productData.get('product_id')  # Assuming 'product_id' is in your JSON payload

#     if not product_id:
#         return {
#             'res': 'False',
#             'msg': 'Product ID is missing in the request'
#         }

#     # Convert product_id to ObjectId
#     product_id = ObjectId(product_id)

#     # Find the existing product with the given product_id
#     existing_product = product_collection.find_one({'_id': product_id})

#     if not existing_product:
#         return {
#             'res': 'False',
#             'msg': 'Product not found for the given product_id'
#         }

#     # Update the existing product with the new data
#     result = product_collection.update_one({'_id': product_id}, {'$set': productData})

#     if result.modified_count > 0:
#         return {
#             'res': 'True',
#             'msg': 'Product updated successfully'
#         }
#     else:
#         return {
#             'res': 'False',
#             'msg': 'Failed to update product'
#         }

# @app.route("/search", methods=['GET'])
# @cross_origin(origin='*')
# def search_type():
#     products = list(product_collection.find())
#     keyword = request.args.get("keyword")
#     search_product=[]
#     if not keyword:
#         return jsonify({"error": "Keyword parameter is missing"}), 400

#     results = [product for product in products if keyword.lower() in product["name"].lower()]
#     for product in products:
#         check=product.get('brand')
#         if check.lower()==keyword.lower():
#             search_product.append(product)
#     #     product['_id'] = str(product.get('_id'))
#     #     list_category.append(product)

#     return search_product


# if __name__ == "__main__":
#     app.run(debug=True)

    