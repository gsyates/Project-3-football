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

def test_get_player_byname(name_player):
    r = requests.post(
        url = url_api+"get_player_byname",
        json = {
            'Name': name_player,
        }
    )
    print(r.content)

def test_add_player():
    r = requests.post(
        url = url_api+"add_player",
        json = {
            "Name": "Kylian Mbappe", 
            "Position": "Centre-Forward", 
            "Age": 18, 
            "Team_from": "Monaco",
            "League_from": "Ligue 1",
            "Team_to": "PSG",
            "League_to": "Ligue 1",
            "Season": "2017-2018",
            "Market_value": 145000000.0,
            "Transfer_fee": 180000000.0
        }
    )
    print(r.content)

test_status_api()
test_get_player_byname("Nicolas Anelka")
test_add_player()
test_get_player_byname("Kylian Mbappe")
