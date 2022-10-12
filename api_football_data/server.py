from flask import Flask, request, render_template, make_response
import pandas as pd
import os
from pymongo import MongoClient
import pymongo
from werkzeug.exceptions import BadRequest,HTTPException, NotFound
from pymongo.errors import ConnectionFailure
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
        if os.path.exists(data["Name"]):
            client = db_connection()
            col = get_col_clientdb(client)
            query = list(col.find(filter={'Name': data["Name"]}))
            client.close()
            return(pprint(query))
    except ValueError:
        raise NotFound("joueur introuvable !")

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000)

