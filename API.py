import requests

response = requests.get("https://api.weatherapi.com/v1/current.json")

data = response.json()

print(data)