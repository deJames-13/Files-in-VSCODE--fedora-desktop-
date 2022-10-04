from operator import le
import requests
import json

response = requests.get("https://randomuser.me/api/?results=10"
)
data = response.json()
for user in data:
    for user_info in data[user]:
        for info in user_info:
            try:
                print(f"{info}: {user_info[info]}\n")
            except TypeError:
                print(user_info)
        
