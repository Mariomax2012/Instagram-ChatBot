import json


# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

# set variables and params
app_id = config["app_id"]
app_secret = config["app_secret"]
redirect_uri = config["redirect_uri"]

url = "https://instagram.com/oauth/authorize"
url = url + "?" + f"client_id={app_id}"
url = url + "&" + f"redirect_uri={redirect_uri}"
url = url + "&" + f"response_type=code"
url = url + "&" + f"scope={('instagram_business_basic,instagram_business_content_publish,instagram_business_manage_messages,instagram_business_manage_comments').replace(',','%2C')}"


print(url)