import json
import requests
import random
import time
from datetime import datetime, timedelta
from flask import Flask
from flask import request


# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

# the messages you will output
message = "This is an automated bot created by this user. They are not available at the moment, but has provided a link for your viewing pleasure in the meantime:"

# message api and cooldown tracker
cooldown = timedelta(hours=24) #cooldown for bot reactivation for specific user
last_reply = {}
user_id = config["user_id"]
url = f"https://graph.instagram.com/v23.0/{user_id}/messages"
headers = {
    "Authorization" : f"Bearer {config["access_token"]}",
    "Content-Type" : "application/json"
}

app = Flask(__name__) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/privacy_policy")
def privacy_policy():
    with open("./privacy_policy.html", "rb") as file:
        privacy_policy_html = file.read()
    return privacy_policy_html

@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
    # automated messaging
    if request.method == "POST":
        try:
            data = request.get_json()
            print(json.dumps(data, indent=4))
            # variables
            isMessage = data.get("entry")[0].get("messaging")[0].get("message")
            recipient_id = int(data["entry"][0]["messaging"][0]["recipient"]["id"])
            sender_id = int(data["entry"][0]["messaging"][0]["sender"]["id"])
            reel = random.choice(config["media_links"])

            # body variables
            text_body = {
                "recipient":{
                    "id": sender_id
                },
                "message":{
                    "text": message
                }
            }
            reel_body = {
                "recipient":{
                    "id": sender_id
                },
                "message":{
                    "text": reel
                }
            }

            if isMessage and recipient_id == user_id:
                if sender_id in last_reply and datetime.now() - last_reply[sender_id] <= cooldown:
                    print("User is still on cooldown!")
                else:
                    post_message = requests.post(url, headers=headers, json=text_body)
                    message_data = post_message.json()
                    print(json.dumps(message_data, indent=4))
                    time.sleep(2)
                    post_message = requests.post(url, headers=headers, json=reel_body)
                    last_reply[sender_id] = datetime.now()
            print(last_reply)

        # this section is for testing the webhook
        except:
            pass
        return "<p>This is POST request, Hello Webhook!</p>"
    if request.method == "GET":
        hub_mode = request.args.get("hub.mode")
        hub_challenge = request.args.get("hub.challenge")
        hub_verify_token = request.args.get("hub.verify_token")
        if hub_challenge:
            return hub_challenge
        else:
            return "<p>This is GET request, Hello Webhook!</p>"
            