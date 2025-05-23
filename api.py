from ctypes import LibraryLoader

import requests
import json
import base64
from base64 import b64encode
import re

url = 'https://geois2.orb.ru/api/resource/8804/feature/'
username = "X2h+YWNrYXRob25fMjc=@#$"
password = "X2h+YWNrYXRob25fMjdfMjU=*&^"

def decrypt(encrypted_text):
    cleaned_text = ''.join(c for c in encrypted_text if c.isalnum() or c in {'+', '/', '='})
    return base64.b64decode(cleaned_text).decode('utf-8')[1] + base64.b64decode(cleaned_text).decode('utf-8')[3:]

def basic_auth(username, password):
    token = b64encode(f"{decrypt(username)}:{decrypt(password)}".encode('utf-8')).decode("ascii")
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