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

## Application functionality - 

### User - 

1. Sign up from the login screen as Customer, enter personal details, username and password.
2. Go to login page, use the same username and password to login
3. Product List page - All the products available will be shown.
4. Click on Add to cart button - Product will be added to cart.
5. User can click on a product, this will go to product view page.
Product view page - <br />
•	User can click all the images shown to see a larger image.
•	Click add to cart button - Product will be added to cart.
6. Click on cart icon from the navigation bar.
Cart page - <br/>
•	Products added to cart will be shown
•	Product quantity can be increased or remove from cart
Product List Page - <br/>
6. Type keyword in search bar and enter.
7. Only products containing the keyword will be returned.
8. Click on any of the Product category in the navigation bar.
9. Products related to the particular category will be shown.
10. If seller puts the cart products on sale - Notification will be shown that product went on sale.

### Seller - 

1. Sign up from the login screen as Customer, enter personal details, username and password.
2. Go to login page, use the same username and password to login.
3. Seller dashboard page will open which lists all the products created by seller.
4. Click on Add to product button.
Add product page - <br/>
•	Fill all the form fields, select images and click "Add product" button to add product.
5. In dashboard page, product can be edited or deleted.
6. Click edit product - Edit product page will open - 
7. Here the seller can change images, put the product on sale or remove sale from product.
8. Click "Edit product button" the product will be edited and changes will be reflected in both seller and user pages.



## API documentation - 

#### Login Endpoint<br />
Description
This API endpoint allows users to authenticate and login to the system using their username and password.

Endpoint - /login

Method - POST

Notes - 
This endpoint uses HTTP POST method, the response contains a res field indicating the success or failure of the login attempt.
Successful login is indicated by "res": "True", while unsuccessful login is indicated by "res": "False".


#### Signup Endpoint

Description
The User Signup API endpoint enables users to register a new account by providing essential information such as user type, email, username, first name, last name, address, phone number, and password. The provided details are then encrypted (optional) and stored in a MongoDB collection.

Endpoint - /signup

Method - POST

Notes - 
•	The API response includes a success message along with the user ID if the signup is successful.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	Optionally, the encrypt function can be used to encrypt sensitive information like usernames and passwords before storage.<br />
•	The document is inserted into the MongoDB collection named collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />


#### Add-Product Endpoint

Description
The Add Product API endpoint allows sellers to add a new product to the database by providing necessary product information. The provided details are then stored in a MongoDB collection designated for products.

Endpoint - /seller/add-product

Method - POST

Notes
•	The API response includes a success message along with the product ID if the product addition is successful.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The document is inserted into the MongoDB collection named product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />


#### Get All-Products Endpoint

Description
The Get All Products API endpoint retrieves information about all products stored in the database. Sellers or other users can use this endpoint to view a list of available products.

Endpoint - /product/all-products

Method - GET

Notes
•	The API response includes a list of product objects with details such as product ID, name, description, price, quantity, and seller.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The document IDs are converted to strings for better compatibility with JSON serialization.<br />
•	The products are fetched from the MongoDB collection named product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />


#### Cart Endpoint

Description
The Add Product to Cart API endpoint allows users to add selected products to their shopping cart. Users can specify the product ID and quantity they wish to add to the cart, and this information is then stored in a MongoDB collection dedicated to shopping carts.

Endpoint - /cart

Method - POST

Notes
•	The API response includes a success message along with the cart item ID if the product addition to the cart is successful.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The document is inserted into the MongoDB collection named cart_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />


#### Category Endpoint

Description
The Get All Products by Category API endpoint retrieves information about all products grouped by category from the database. Users can use this endpoint to view a list of available products organized by their respective categories.

Endpoint - /category

Method - POST

Notes
•	The API response includes a list of product objects with details such as product ID, name, description, price, quantity, seller, and category.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The document IDs are converted to strings for better compatibility with JSON serialization.<br />
•	The products are fetched from the MongoDB collection named product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />

#### Search Endpoint

Description
This will return all the products from the Database based on the keyword provided by the user.

Endpoint - /search

Method - POST

Notes
•	The API response includes a list of product objects with details such as product ID, name, description, price, quantity, seller, and category.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The document IDs are converted to strings for better compatibility with JSON serialization.<br />
•	The products are fetched from the MongoDB collection named product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />


#### Orders Endpoint

Description
The Get Order Details API endpoint retrieves information about user orders and includes details about the products in the orders. Users can use this endpoint to view a list of their orders along with associated product details.

Endpoint - /orders

Method - GET

Notes - 
•	The API response includes a list of order objects with details such as order ID, product ID, quantity, product image data, brand, product description, price, and discount.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The documents are retrieved from the MongoDB collections named cart_collection and product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />

#### Show notification Endpoint

Description
This endpoint will alert the user if there are product in cart which went on sale.

Endpoint - /sale-notification

Method - GET

Notes - 
•	The API response includes a list of order objects with details such as order ID, product ID, quantity, product image data, brand, product description, price, and discount of the product which went on sale.<br />
•	In case of an error, an appropriate error message is returned.<br />
•	The documents are retrieved from the MongoDB collections named cart_collection and product_collection.<br />
•	Ensure to handle errors in the application based on the received response.<br />













