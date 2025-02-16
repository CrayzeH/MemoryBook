import requests

def http_get_request(url: str, params: dict = None, headers: dict = None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Проверка на ошибки
        return response.json()  # Возвращаем JSON-ответ
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

# Пример использования:
url = "http://example.com/api/data"
params = {"key": "value"}
headers = {"Authorization": "Bearer your_token"}

data = http_get_request(url, params=params, headers=headers)
if data:
    print("Данные получены:", data)