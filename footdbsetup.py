from pymongo import MongoClient
#from utils import get_my_password, get_my_username
from pprint import pprint


client = MongoClient(
    host='127.0.0.1',
    port=27017,
    username='root',
    password='example',
    authSource='admin'
)

#db = client['footballclient']
#col = db['football']

#pprint(col.find_one())
print(client)
