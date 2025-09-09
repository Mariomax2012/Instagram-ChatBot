# Instagram-ChatBot
Automated chatbot for instagram. Can be customized however you please. 

Pre-setup
- type in console: "pip install flask" "pip install requests"
- Download ngrok https://ngrok.com/downloads/windows?tab=download (Download for Windows 64-Bit)

1. Create Application

- Log into https://developers.facebook.com
- Go to Apps and Create App (Make sure to select Business for App Type)
- Add the Instagram product to your app

2. Setup Instagram API (Link Instagram Account)

- Select Instagram under products, and "API setup with Instagram login." Near the top of the page you will see your app name, ID, and secret.
- To generate access tokens, link your instagram account (must be a business account, if not, you can change it in instagram's account settings)
- Once linked, your account name and ID will be shown. Generate your access token and turn webhook subscriptions on.

3. Setup Instagram API (Launch Web Application)

- Open command prompt in the Instagram-ChatBot folder, make sure to install flask
- In the console, type: "set FLASK_APP=webhook.py", then, type "flask run"
- A url will be displayed: "running on http://...." copy the url. Paste it into your browser to ensure functionality.
- Without closing your current cmd prompt, open a new one in the same folder.
- Type "ngrok http {port number}" In this case, since my url was http://127.0.0.1:5000, the port number would be 5000
- Your web app will go live, and your url will be where it says "Forwarding" ("http://....ngrok-free.app") open the url
- Make sure to keep both cmd prompts running in the background

4. Setup Instagram API (Configure Webhooks)

- Navigate back to your Facebook Application, and in the Instagram Procuct tab
- Under "2. Configure webhooks", paste your ngrok url under "Callback URL" and add "/webhook" at the end. You will also need to make your own password (verify token). Verify and save
- Manage webhooks. You can test different webhook fields. Once you test, it will show up on your flask.

5. Setup Instagram API (Instagram Business Login)

- Under "3. Set up Instagram Business Login" and under "Embed URL", paste your ngrok url (without /webhook)
- Navigate to app settings in the side bar, and then click "Basic"
- Under "Privacy Policy URL" paste your ngrok url, but add "/privacy_policy" at the end. Save changes.
- On the top bar, switch "App Mode: Development" to live.

6. Configuration 

- Go to the insta_config.json file
- Fill in app_id, app_secret, user_id and redirect_url (ngrok url).
- To generate out access token, navigate to the get_auth_code file and click run. Click on the link generated.
- Once you allow instagram to connect, click on the url in the search bar. Copy the string after "code="
- Patse that code in "auth_code" in the insta_config file
- Then, go to the get_token file and run. Your access token will be generated. (You can see your token in the config file next to "access_token")

7. Guide

- Everything has been setup and you can start using the bot. Currently, the bot is setup to detect incoming messages and giving an automated response. It also sends random links from a list which you can customize under the insta_config file where it says "media_links"
- The get_user_info file gets your user information.
- The send_messages file lets you send a message to an instagram user from this very console. To get a user's instagram ID, you must send them a message or recieve a message from them for it to show up in your cmd prompt in flask. There you can see the receipient/sender ID's.
- You can fully customize the bot however you please. To reactivate the bot you must go through steps 3-6 again. Although you won't have to re-input your app id, secret, or user_id again if using the same account.