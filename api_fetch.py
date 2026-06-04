import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Company:", user["company"]["name"])
    print("-" * 30)