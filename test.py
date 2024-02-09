import requests

response = requests.get(
    "http://localhost:5000/hello",
    params={
        'value' : 'creating api for myself'
    }
)