from flask import Flask, jsonify, render_template, request
# from database import db as DB
import json


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/' , methods =['GET'])
def home():
    return "<h1> My name is Mohit </h1>"

@app.route('/test',methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        return "<h1> My name is Mohit </h1>"
    if(request.method == 'POST'):
        data = request.get_json()
        print(type(data))
        print(data)
        print(jsonify(data) )
        return "<h1> Great Success</h1>" , 200
app.run()