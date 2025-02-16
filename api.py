import requests
import json
from base64 import b64encode

url = 'https://geois2.orb.ru/api/resource/8804/feature/'
username = "hackathon_27"
password = "hackathon_27_25"

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

def get_warrior():
    headers = {
        'Accept': '*/*',
        'Authorization': basic_auth(username, password),
        'id': '1'
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    first = response[0]
    second = response[1]
    third = response[2]
    first, second, third = first['fields'], second['fields'], third['fields']
    return first, second, third