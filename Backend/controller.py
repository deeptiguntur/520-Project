# controllers.py
from flask import request, jsonify
from cryptography.fernet import Fernet
from Models import collection, product_collection, cart_collection
from bson import ObjectId

def encrypt(text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text,key
def decrypt(encrypted_text,key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

def login():
    loginData = request.get_json()
    user = loginData['username']
    passw = loginData['password']

    user_entry = collection.find_one({'username': user})

    if user_entry:
        decrypted = decrypt(user_entry['password'],user_entry['key'])
        
        if decrypted == passw:
            print("Login successful")
            return {'res': 'True', 'user_type': user_entry['user_type'], 'user_id': str(user_entry.get('_id'))}
            # Add code for successful login, e.g., return a response or set a session variable
        else:
            print("Incorrect password")
            return {'res': 'False'}
            # Add code for incorrect password, e.g., return an error response
    else:
        print("User not found")
        return {'res': 'False'}
        # Add code for user not found, e.g., return an error response
    

def signup():
    signupData = request.get_json()
    password_encrypted,key=encrypt(signupData['password'])
    user_data = {
        'user_type': signupData['user_type'],
        'email': signupData['email'],
        'username': signupData['username'],
        'first_name': signupData['first_name'],
        'last_name': signupData['last_name'],
        'address': signupData['address'],
        'phone': signupData['phone'],
        'password': password_encrypted,
        'key':key
    }

    result = collection.insert_one(user_data)
    if result.inserted_id:
        return {'res': 'True', 'msg': "Signup successfull!"}
    else:
        return {'res': 'False', 'msg': "Error occurred during signup"}

# Define other controller functions here for product addition, cart, etc.

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
            'res': 'False',
            'msg': "Error occurred during adding product"
        }
def product_cart():
    cart_data=request.get_json()
    product_id=cart_data['product_id']
    cart_quantity = cart_data['quantity']
    orders = list(cart_collection.find())
    flag=0
    for order in orders:
        
        check_order = str(order.get('product_id'))
        if check_order == product_id:
            condition = {'product_id': check_order}

            # Specify the update operation
            update_operation = {'$set': {'quantity': cart_quantity}}

            # Update the document in the collection
            cart_update = cart_collection.update_one(condition, update_operation)
            flag=1

    if flag==0:
        cart_insert = {
            'product_id': product_id,
            'quantity': cart_quantity,
        }
        ##Insert the document into the MongoDB collection
        cart_result = cart_collection.insert_one(cart_insert)

    if flag==1 or cart_result.inserted_id:
        return {
            'res': 'True',
            'msg': "Added Product in Cart"
        }
    else:
        return {
            'res': 'False',
            'msg': "Error occurred while adding product in cart"
        }
def getAllProducts():
    # products = product_collection.find().toArray()
    products = list(product_collection.find())
    product_list = []
    for product in products:
        product['_id'] = str(product.get('_id'))
        product_list.append(product)
    return product_list 

def categorypage():
    products = list(product_collection.find())
    productData = request.get_json()
    category_type = productData.get('category')  # Assuming 'product_id' is in your JSON payload
    list_category = []
    for product in products:
        if product.get('category')==category_type:
            product['_id'] = str(product.get('_id'))
            list_category.append(product)
    return list_category 

def orderdetails():
    orders = list(cart_collection.find())
    order_list = []
    products = list(product_collection.find())  # Retrieve all products

    # Add image data to each order based on product_id
    for order in orders:
        for product in products:
            product['_id']=str(product.get('_id'))
            if product['_id'] == order['product_id']:
                order['_id'] = str(order.get('_id'))
                order['imgData'] = product.get('imgData')
                order['brand'] = product.get('brand')
                order['productDesc']=product.get('productDesc')
                order['price']=product.get('price')
                order['discount']=product.get('discount')
                order['productName']=product.get('productName')
                order['sale']=product.get('sale')
                order_list.append(order)
    return order_list 

##editing products
def editProduct():
    productData = request.get_json()
    product_id = productData.get('product_id')  # Assuming 'product_id' is in your JSON payload

    if not product_id:
        return {
            'res': 'False',
            'msg': 'Product ID is missing in the request'
        }

    # Convert product_id to ObjectId
    product_id = ObjectId(product_id)

    # Find the existing product with the given product_id
    existing_product = product_collection.find_one({'_id': product_id})

    if not existing_product:
        return {
            'res': 'False',
            'msg': 'Product not found for the given product_id'
        }
    
    if productData['sale']:
        productData['saleNotification'] = True

    # Update the existing product with the new data
    result = product_collection.update_one({'_id': product_id}, {'$set': productData})

    if result.modified_count > 0:
        return {
            'res': 'True',
            'msg': 'Product updated successfully'
        }
    else:
        return {
            'res': 'False',
            'msg': 'Failed to update product'
        }

def notifySale():
    cart_data = cart_collection.find()
    notif_data = []
    for product in cart_data:
        product_data = product_collection.find_one(ObjectId(product['product_id']))
        if 'saleNotification' in product_data:
            result = product_collection.update_one({'_id': ObjectId(product['product_id'])}, {'$unset' : { 'saleNotification' : True}})
            product_data['_id'] = str(product_data.get('_id'))
            notif_data.append(product_data)
    if len(notif_data):
        return {
            'res': 'True',
            'product': notif_data
        }

    return {
        'res': 'False'
    }



##search products
def search_type():
    products = list(product_collection.find())
    Data_key = request.get_json()
    keyword=Data_key.get('keyword')
    search_product=[]
    if not keyword:
        for product in products:
            product['_id'] = str(product.get('_id'))
            search_product.append(product)
    else:

        # results = [product for product in products if keyword.lower() in product["name"].lower()]
        for product in products:
            check=product.get('brand')
            checkName=product.get('productName')
            if check.lower()==keyword.lower() or keyword.lower() in checkName.lower():
                product['_id'] = str(product.get('_id'))
                search_product.append(product)
        #     product['_id'] = str(product.get('_id'))
        #     list_category.append(product)

    return search_product

