import requests

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint , params={"abc": 123},json={"query": "Hello World"})
# HTTP Request -> HTML
# REST API HTTP Request -> JSON (JavaScript Object Notation) (in other words formatted data that python can use)
#print(get_response.text)
print(get_response.json())
#print(get_response.status_code)
