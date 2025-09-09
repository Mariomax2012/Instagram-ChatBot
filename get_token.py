import requests
import json


# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

# set variables and params
app_id = config["app_id"]
app_secret = config["app_secret"]
redirect_uri = config["redirect_uri"]
auth_code = config["auth_code"]

# run code, access token will be granted and saved to config file
url_token = "https://api.instagram.com/oauth/access_token"
params = {
    "client_id" : app_id,
    "client_secret" : app_secret,
    "grant_type" : "authorization_code",
    "redirect_uri" : redirect_uri,
    "code" : auth_code
} 

response = requests.post(url_token, params)
data = response.json()
print(json.dumps(data, indent=4))

user_access_token = data["access_token"]

long_url = "https://graph.instagram.com/access_token"
long_params = {
    "grant_type" : "ig_exchange_token",
    "client_secret" : app_secret,
    "access_token" : user_access_token
}

long_response = requests.get(long_url, long_params)
long_data = long_response.json()
print(json.dumps(long_data, indent=4))

# saves "access_token" to config file
config["access_token"] = long_data["access_token"]
with open("insta_config.json", "w") as file:
    json.dump(config, file, indent=4)
