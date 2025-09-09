import requests
import json

# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

url = f"https://graph.instagram.com/v23.0/{config["user_id"]}/media?access_token={config["long_token"]}"

response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=4))