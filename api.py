import requests

url = 'https://geois2.orb.ru/resource/8805/display?panel=layers'
headers = {
    'Accept' : '/',
    'Authorization': 'hackathon_27:hackathon_27_25'
}

response = requests.get(url, headers=headers)
print(response)