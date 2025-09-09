import requests
import json


# load config file
with open("insta_config.json", "r") as file:
    config = json.load(file)

# the id of person you are sending to, text, image/gif, and video/audio url's
recipient_id = 17841403703599916
text_message = "dude"
# png, jpeg, gif (max 8MB)
image_gif_url = ""
# mp4, ogg, avi, mov, webm (max 25MB)
audio_video_url = "" 


url = f"https://graph.instagram.com/v23.0/{config["user_id"]}/messages"
headers = {
    "Authorization" : f"Bearer {config["access_token"]}",
    "Content-Type" : "application/json"
}
text_body = {
            "recipient":{
                "id": recipient_id
            },
            "message":{
                "text": text_message
            }
    }
image_body = {
            "recipient":{
                "id": recipient_id
            },
            "message":{
                "attachment":{
                    "type": "image",
                    "payload":{
                        "url": image_gif_url,
                }
            }
        }
    }
video_body = {
           "recipient":{
               "id": recipient_id
           },
           "message":{
              "attachment":{
               "type":"video",  # or set to audio
               "payload":{
                 "url":audio_video_url,
               }
             }
          }
        }

# change "json=" field to the type of message you will be sending (text_body, image_body, video_body)
response = requests.post(url, headers=headers, json=text_body)
data = response.json()
print(json.dumps(data, indent=4))