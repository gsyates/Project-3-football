import os
import requests
#import pytest
#give the program time to get the api up and running before running the tests
import time
time.sleep(8)

api_address = '172.28.1.2'
#api_address = 'localhost'
# port de l'API
api_port = 8000

url_api = 'http://{address}:{port}/'.format(address=api_address, port=api_port)

def test_status_api():
    r = requests.get(
        url = url_api+"status",
    )
    status_code = r.status_code
    print(status_code)

def test_get_player_byname():
    r = requests.post(
        url = url_api+"get_player_byname",
        json = {
            'Name': "Nicolas Anelka",
        }
    )
    print(r.content)

test_status_api()
test_get_player_byname()

