from pymongo import MongoClient
#from utils import get_my_password, get_my_username
from pprint import pprint
from pymongo.errors import ConnectionFailure

client = MongoClient('mongodb://172.20.0.3:27017/')

try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
except ConnectionFailure:
    print("Server not available")

#db = client['footballclient']
#col = db['football']

#pprint(col.find_one())
#print(client)

#from pprint import pprint
#from pymongo import MongoClient

#client = MongoClient('localhost', port=27017)

#db = client.admin

#server = db.command("serverStatus")
#pprint(server)
