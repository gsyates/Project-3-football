from pymongo import MongoClient
#from utils import get_my_password, get_my_username
from pprint import pprint
from pymongo.errors import ConnectionFailure

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
col.insert_one({'example': 123})
pprint(col.find_one())

client.close()

