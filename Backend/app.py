from flask import Flask
app = Flask(__name__)
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import request, jsonify
from flask_cors import CORS, cross_origin

uri = "mongodb+srv://dguntur:KxvqWuZLmbTE0U7O@cluster0.5wory1k.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
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
    print(loginData['username'])
    print(loginData['password'])
    return "True"
    
