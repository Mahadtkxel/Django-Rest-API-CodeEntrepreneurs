import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "this field is",
    "content": "creating new record",
    "price": 420.69,
}

get_response = requests.post(endpoint, json=data)


print(get_response.json())