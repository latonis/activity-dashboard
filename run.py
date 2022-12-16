import requests
import json
import dotenv
                
tokenURL = "https://www.strava.com/api/v3/oauth/token"
config = dotenv.dotenv_values(".env")
tokens = json.load(open(".tokens", "r"))

data = {
    "client_id": config["CLIENT_ID"],
    "client_secret": config["STRAVA_SECRET"],
    "refresh_token": tokens["refresh_token"],
    'grant_type': "refresh_token",
}

req = requests.post(tokenURL, data=data)
reqJSON = req.json()

print(reqJSON)



