import requests
import json
import dotenv

def getAccessToken() -> dict: 
    tokenURL = "https://www.strava.com/api/v3/oauth/token"
    config = dotenv.dotenv_values(".env")
    tokens = json.load(open(".tokens", "r"))

    tokenData = {
        "client_id": config["CLIENT_ID"],
        "client_secret": config["STRAVA_SECRET"],
        "refresh_token": tokens["refresh_token"],
        "grant_type": "refresh_token",
    }

    req = requests.post(tokenURL, data=tokenData)

    reqJSON = req.json()

    with open (".tokens", "w") as f:
        f.write(json.dumps(reqJSON))

    return reqJSON

if __name__ == "__main__":
    print(getAccessToken())