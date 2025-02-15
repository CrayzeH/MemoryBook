import requests

url = 'https://geois2.orb.ru/api/component/feature_layer/mvt?resource=8804&z={z}&x={x}&y={y}'
headers = {
    'Authorization': 'hackathon_27:hackathon_27_25'
}

response = requests.get(url, headers=headers)
print(response)