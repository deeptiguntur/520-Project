from flask import Flask
app = Flask(__name__)
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import request, jsonify
from flask_cors import CORS, cross_origin

uri = "mongodb+srv://anamikaghosh:KivaL2QA9mYb89gY@cluster0.uela1gh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Shopfinity']  # Replace '
collection = db['Login_Details']  # Replace
# Create a new client and connect to the server

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
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     # Check if the username and password exist in MongoDB
    #     user_entry = collection.find_one({'username': username, 'password': password})

    #     if user_entry:
    #         print("Login successful for user ")
    #         print(username)
    #     else:
    #         return "Invalid username or password. Please try again."
    loginData = request.get_json()
    # print(loginData['username'])
    # print(loginData['password'])
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

    return "True"
if __name__ == "__main__":
    app.run(debug=True)

    

