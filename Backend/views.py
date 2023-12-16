# views.py
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from controller import login, signup, addProduct, product_cart, getAllProducts, categorypage, orderdetails,editProduct,search_type, notifySale

app = Flask(__name__)
CORS(app)
#home page
@app.route("/")
def home():
    return "Hello, Flask!"
#ogin page 
@app.route("/login", methods=['POST'])
@cross_origin(origin='*')
def login_route():
    return login()
#sign up page for customers and sellers
@app.route('/signup', methods=['POST'])
@cross_origin(origin='*')
def signup_route():
    return signup()
#adding the products into seller page
@app.route("/seller/add-product", methods=['POST'])
@cross_origin(origin='*')
def addProduct_route():
    return addProduct()
#cart details for the customers
@app.route('/cart', methods=['POST'])
@cross_origin(origin='*')
def product_cart_route():
    return product_cart()
#displaying all the products in home page
@app.route("/product/all-products", methods=['GET'])
@cross_origin(origin='*')
def getAllProducts_route():
    products = getAllProducts()
    return products

@app.route("/category", methods=['POST'])
@cross_origin(origin='*')
def categorypage_route():
    categories = categorypage()
    return categories
#orders page for the customer and the way to go for payment page 
@app.route("/orders", methods=['GET'])
@cross_origin(origin='*')
def orderdetails_route():
    orders = orderdetails()
    return orders
#editing the products details only allowed for sellers
@app.route("/editproduct", methods=['POST'])
@cross_origin(origin='*')
def editProduct_route():
    return editProduct()
#editing the products details only allowed for sellers
@app.route("/search", methods=['POST'])
@cross_origin(origin='*')
def search_type_route():
    products_search=search_type()
    return products_search
@app.route("/sale-notification", methods=['GET'])
@cross_origin(origin='*')
def sale_notification_route():
    sale_product=notifySale()
    return sale_product

if __name__ == "__main__":
    app.run(debug=True)

