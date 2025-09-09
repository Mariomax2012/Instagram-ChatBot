import requests
import json

# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

# set variables and params
access_token = config["access_token"]
url = "https://graph.instagram.com/v23.0/me"
params = {
    "fields" : ("id,user_id,username,name,followers_count,follows_count,media_count,account_type,profile_picture_url"),
    "access_token" : access_token
}

# get and print data
response = requests.get(url, params)
data = response.json()
print(json.dumps(data, indent=4))

# saves "user_id" to config file
config["user_id"] = int(data["user_id"].strip('"'))
with open("insta_config.json", "w") as file:
    json.dump(config, file, indent=4)