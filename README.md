# 520-Project

## E-Commerce site - Shopfinity

Frontend - Angular <br />
Backend - Python/Flask <br />
Database - MongoDB <br />
<br />

### To run Frontend - <br />
1. cd Frontend/shopfinity/src
2. npm start

### To run Backend - <br />
### MVC demonstration  ###
Mac-<br />

1.export FLASK_APP=views.py
2.export FLASK_ENV=development
flask run 
<br />
Windows - <br />

1. $env:FLASK_APP = "views.py"
2. $env:FLASK_ENV = "development"
3. python -m flask run
<br />

## API documentation - 
Login Endpoint<br />
Description<br />
This API endpoint allows users to authenticate and login to the system using their username and password.

Endpoint<br />
/login<br />

Method
POST

Request Parameters
Content Type: application/json
Data Format:
{
    "username": "seller1",
    "password": "123"
}

Response
   Success Response:
Status Code: 200 OK
Data Format:
{
    "res": "True"
}
res: Indicates the result of the login attempt. "True" signifies a successful login.
   Error Response:
Status Code: 200 OK
Data Format:
{
    "res": "False"
}
res: Indicates the result of the login attempt. "False" signifies an unsuccessful login

Notes
This endpoint uses HTTP POST method to securely transmit user credentials.
The response contains a res field indicating the success or failure of the login attempt.
Successful login is indicated by "res": "True", while unsuccessful login is indicated by "res": "False".


Signup Endpoint

Description
The User Signup API endpoint enables users to register a new account by providing essential information such as user type, email, username, first name, last name, address, phone number, and password. The provided details are then encrypted (optional) and stored in a MongoDB collection.

Endpoint
POST /signup

Method
POST

Headers
•	Content-Type: application/json
Request Body
The request body must contain a JSON object with the following parameters:
•	user_type (string): Type of user account (e.g., "customer", "admin").
•	email (string): User's email address.
•	username (string): User's chosen username.
•	first_name (string): User's first name.
•	last_name (string): User's last name.
•	address (string): User's address.
•	phone (string): User's phone number.
•	password (string): User's chosen password.
Example:
{
    "user_type": "customer",
    "email": "user@example.com",
    "username": "user123",
    "first_name": "John",
    "last_name": "Doe",
    "address": "123 Main St, City",
    "phone": "555-1234",
    "password": "secretpassword"
}

Response
   Success Response
•	Status Code: 200 OK
{
    "message": "Signup successful! User ID: 1"
}

  Error Response
•	Status Code: 500 Internal Server Error
{
    "error": "Error occurred during signup"
}

Notes
•	The API response includes a success message along with the user ID if the signup is successful.
•	In case of an error, an appropriate error message is returned.
•	Optionally, the encrypt function can be used to encrypt sensitive information like usernames and passwords before storage.
•	The document is inserted into the MongoDB collection named collection.
•	Ensure to handle errors gracefully in your application based on the received response.


Add-Product Endpoint

Description
The Add Product API endpoint allows sellers to add a new product to the database by providing necessary product information. The provided details are then stored in a MongoDB collection designated for products.

Endpoint
POST /seller/add-product

Method
POST

Headers
•	Content-Type: application/json
Request Body
The request body must contain a JSON object with the following parameters:
•	productName (string): Name of the product.
•	productDescription (string): Description of the product.
•	price (number): Price of the product.
•	quantity (integer): Quantity of the product available.
•	seller (string): Name or identifier of the seller.
Example:
{
    "productName": "Widget X",
    "productDescription": "A high-quality widget",
    "price": 19.99,
    "quantity": 100,
    "seller": "Seller123"
}

Response
   Success Response
•	Status Code: 200 OK
{
    "res": "True",
    "msg": "Added Product!: {1}"
}

   Error Response
•	Status Code: 500 Internal Server Error
{
    "res": "True",
    "msg": "Error occurred during adding product"
}

Notes
•	The API response includes a success message along with the product ID if the product addition is successful.
•	In case of an error, an appropriate error message is returned.
•	The document is inserted into the MongoDB collection named product_collection.
•	Ensure to handle errors gracefully in your application based on the received response.


All-Products Endpoint

Description
The Get All Products API endpoint retrieves information about all products stored in the database. Sellers or other users can use this endpoint to view a list of available products.

Endpoint
GET /product/all-products

Method
GET

Response
   Success Response
•	Status Code: 200 OK
[
    {
        "_id": "product_id_1",
        "productName": "Widget X",
        "productDescription": "A high-quality widget",
        "price": 19.99,
        "quantity": 100,
        "seller": "Seller123"
    },
    {
        "_id": "product_id_2",
        "productName": "Gadget Y",
        "productDescription": "An innovative gadget",
        "price": 29.99,
        "quantity": 50,
        "seller": "Seller456"
    },
    ...
]

   Error Response
•	Status Code: 500 Internal Server Error
{
    "error": "Error occurred while fetching products"
}

Notes
•	The API response includes a list of product objects with details such as product ID, name, description, price, quantity, and seller.
•	In case of an error, an appropriate error message is returned.
•	The document IDs are converted to strings for better compatibility with JSON serialization.
•	The products are fetched from the MongoDB collection named product_collection.
•	Ensure to handle errors gracefully in your application based on the received response.


Cart Endpoint

Description
The Add Product to Cart API endpoint allows users to add selected products to their shopping cart. Users can specify the product ID and quantity they wish to add to the cart, and this information is then stored in a MongoDB collection dedicated to shopping carts.

Endpoint
POST /cart

Method
POST

Headers
•	Content-Type: application/json

Request Body
The request body must contain a JSON object with the following parameters:
•	_id (string): ID of the product to be added to the cart.
•	quantity (integer): Quantity of the product to be added to the cart.

Example:
{
    "_id": "product_id_1",
    "quantity": 2
}

Response
   Success Response
•	Status Code: 200 OK
{
    "res": "True",
    "msg": "Added Product in Cart: {cart_inserted_id}"
}
   Error Response
•	Status Code: 500 Internal Server Error
{
    "res": "False",
    "msg": "Error occurred while adding product in cart"
}

Notes
•	The API response includes a success message along with the cart item ID if the product addition to the cart is successful.
•	In case of an error, an appropriate error message is returned.
•	The document is inserted into the MongoDB collection named cart_collection.
•	Ensure to handle errors gracefully in your application based on the received response.


Category Endpoint

Description
The Get All Products by Category API endpoint retrieves information about all products grouped by category from the database. Users can use this endpoint to view a list of available products organized by their respective categories.

Endpoint
GET /category

Method
GET

Headers
•	None
Response
   Success Response
•	Status Code: 200 OK

[
    {
        "_id": "product_id_1",
        "productName": "Widget X",
        "productDescription": "A high-quality widget",
        "price": 19.99,
        "quantity": 100,
        "seller": "Seller123",
        "category": "Electronics"
    },
    {
        "_id": "product_id_2",
        "productName": "Gadget Y",
        "productDescription": "An innovative gadget",
        "price": 29.99,
        "quantity": 50,
        "seller": "Seller456",
        "category": "Gadgets"
    },
    ...
]
   Error Response
•	Status Code: 500 Internal Server Error
{
    "error": "Error occurred while fetching products by category"
}
Notes
•	The API response includes a list of product objects with details such as product ID, name, description, price, quantity, seller, and category.
•	In case of an error, an appropriate error message is returned.
•	The document IDs are converted to strings for better compatibility with JSON serialization.
•	The products are fetched from the MongoDB collection named product_collection.
•	Ensure to handle errors gracefully in your application based on the received response.


Orders Endpoint

Description
The Get Order Details API endpoint retrieves information about user orders and includes details about the products in the orders. Users can use this endpoint to view a list of their orders along with associated product details.

Endpoint
GET /orders

Method
GET


Headers
•	None
Response
   Success Response
•	Status Code: 200 OK
[
    {
        "_id": "order_id_1",
        "product_id": "product_id_1",
        "quantity": 2,
        "imgData": "base64_image_data_1",
        "brand": "Brand A",
        "productDesc": "Description of Product A",
        "price": 19.99,
        "discount": 5
    },
    {
        "_id": "order_id_2",
        "product_id": "product_id_2",
        "quantity": 1,
        "imgData": "base64_image_data_2",
        "brand": "Brand B",
        "productDesc": "Description of Product B",
        "price": 29.99,
        "discount": 10
    },
    ...
]

   Error Response
•	Status Code: 500 Internal Server Error
{
    "error": "Error occurred while fetching order details"
}

Notes
•	The API response includes a list of order objects with details such as order ID, product ID, quantity, product image data, brand, product description, price, and discount.
•	In case of an error, an appropriate error message is returned.
•	The documents are retrieved from the MongoDB collections named cart_collection and product_collection.
•	Ensure to handle errors gracefully in your application based on the received response.













