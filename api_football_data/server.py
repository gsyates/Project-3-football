from flask import Flask, request, render_template, make_response
import pandas as pd
import os
from pymongo import MongoClient
import pymongo
from pprint import pprint
from flask import make_response
from werkzeug.exceptions import BadRequest,HTTPException, NotFound
from pymongo.errors import ConnectionFailure
import json
import time
time.sleep(3)

server = Flask(__name__)

def db_connection():
    client = MongoClient(
        host='172.28.1.1',
        port=27017,
        username='football',
        password='mdpfootball',
        authSource='admin'
    )
    return client

def get_col_clientdb(client):
    client = db_connection()
    db = client['footballclient']
    col = db['football']   
    return col

@server.route('/')
def index():
    try:
        return 'Hello World from a containerized server'
    except HTTPException as e:
        return e

@server.route('/status')
def testApi():
    try:
        return 'API launched !'
    except HTTPException as e:
        return e

@server.route('/mongodbstatus')
def testMongodb():
    try:
        client = db_connection()
        print("Connection Successful")
    except ConnectionFailure:
        print("Connection failed")

@server.route('/get_player_byname', methods=["POST"])
def get_player():
    try:
        data = request.get_json()
        client = db_connection()
        col = get_col_clientdb(client)
        query = list(col.find(filter={'Name': data["Name"]}))
        return make_response(json.dumps(query,default=str))
    except ValueError:
        raise NotFound("joueur introuvable !")

@server.route('/add_player', methods=["POST"])
def add_player():
    data = request.get_json()
    client = db_connection()
    col = get_col_clientdb(client)
    results = col.insert_one({"Name": data["Name"], "Position": data["Position"], "Age": data["Age"], "Team_from": data["Team_from"], "League_from": data["League_from"], "Team_to": data["Team_to"], "League_to": data["League_to"], "Season": data["Season"], "Market_value": data["Market_value"], "Transfer_fee": data["Transfer_fee"]})
    return make_response(json.dumps(results.inserted_id,default=str))

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000)

