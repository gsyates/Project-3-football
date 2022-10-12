from pymongo import MongoClient, mongoimport
#from utils import get_my_password, get_my_username
from pprint import pprint
from pymongo.errors import ConnectionFailure
import pymongo
import csv
import pandas as pd
import json

client = MongoClient(
    host='172.28.1.1',
    port=27017,
    username='football',
    password='mdpfootball',
    authSource='admin'
)

try:
  print("Connection Successful")
except ConnectionFailure:
  print("Connection failed")

db = client['footballclient']
col = db['football']

#method2 using python and import many
df=pd.read_csv('top250-00-19.csv', header=0)
data=df.to_dict(orient="records")
result=col.insert_many(data)

#col.delete_one(filter={'_id': 1})
print('hello gerry')

query = list(col.find(filter={'Age': 27})
pprint (query)

client.close()

