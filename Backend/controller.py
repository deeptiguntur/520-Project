# controllers.py
from flask import request, jsonify
from cryptography.fernet import Fernet
from Models import collection, product_collection, cart_collection

# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

# def encrypt(text):
#     encrypted_text = cipher_suite.encrypt(text.encode())
#     return encrypted_text

# def decrypt(encrypted_text):
#     decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
#     return decrypted_text
key = Fernet.generate_key()
cipher_suite = Fernet(key)
def encrypt(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text
def decrypt(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

def login():
    loginData = request.get_json()
    user = loginData['username']
    passw = loginData['password']

    user_entry = collection.find_one({'username': user})
    print(user_entry)

    if user_entry:
        decrypted = decrypt(user_entry['password'])
        print(decrypted)
        
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
    user_data = {
        'user_type': signupData['user_type'],
        'email': signupData['email'],
        'username': signupData['username'],
        'first_name': signupData['first_name'],
        'last_name': signupData['last_name'],
        'address': signupData['address'],
        'phone': signupData['phone'],
        'password': encrypt(signupData['password'])
    }

    result = collection.insert_one(user_data)
    if result.inserted_id:
        return {'res': 'True', 'msg': "Signup successful!"}
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
    quantity = cart_data['quantity']
    cart_insert = {
        'product_id': product_id,
        'quantity': quantity,
    }
    ##Insert the document into the MongoDB collection
    cart_result = cart_collection.insert_one(cart_insert)

    if cart_result.inserted_id:
        return {
            'res': 'True',
            'msg': "Added Product in Cart: {}".format(cart_result.inserted_id)
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
    list_category = []
    for product in products:
        product['_id'] = str(product.get('_id'))
        list_category.append(product)
    return list_category 

def orderdetails():
    orders = list(cart_collection.find())
    order_list = []
    # for order in orders:
    #     order['_id'] = str(order.get('_id'))
    #     order_list.append(order)
    # return order_list 
    products = list(product_collection.find())  # Retrieve all products

    # Add image data to each order based on product_id
    print(orders)
    for order in orders:
        for product in products:
            product['_id']=str(product.get('_id'))
            if product['_id'] == order['product_id']:
                print("Hi")
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
##search products
def search_type():
    products = list(product_collection.find())
    keyword = request.args.get("keyword")
    search_product=[]
    if not keyword:
        return jsonify({"error": "Keyword parameter is missing"}), 400

    results = [product for product in products if keyword.lower() in product["name"].lower()]
    for product in products:
        check=product.get('brand')
        if check.lower()==keyword.lower():
            search_product.append(product)
    #     product['_id'] = str(product.get('_id'))
    #     list_category.append(product)

    return search_product

