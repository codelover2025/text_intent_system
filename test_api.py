import requests
url = "http://127.0.0.1:5000/api/predict"
data = {
    "key": "demo-k001ey-",
    "guid": "12345",
    "text": "I need a PHP vendor."
}
response = requests.post(url, json=data)
print(response.json())