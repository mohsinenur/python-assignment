'''
Created on Feb 20, 2020

@author: CS6252
'''
from flask import Flask, request
from names import Names
from name_db import NameDB
import json

app = Flask(__name__)
name_db = NameDB()
names = Names(name_db.read_names())

@app.route('/names')
def get_names():
    all_names = names.get_all()
    return json.dumps(all_names), 200;

@app.route('/name/<string:name>')
def get_single_name(name):
    single_names = names.get(name)
    if single_names:
        return json.dumps(single_names), 200
    else:
        return json.dumps({"error": "No name found"}), 400;

@app.route('/name', methods=['POST'])
def add_new_name():
    data = {"name": "Harper", "ranking": 9, "gender": ["M", "F"]}
    response = names.add(data)
    if response != None:
        return json.dumps(response), 201;
    else:
        return json.dumps({"error": "Invalid keys"}), 400;

