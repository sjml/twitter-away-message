import json
from datetime import datetime, timezone

import tweepy

creds = json.load(open("./credentials.json", "r"))
config = json.load(open("./config.json", "r"))

auth = tweepy.OAuthHandler(creds["API_KEY"], creds["SECRET_KEY"])
auth.set_access_token(creds["ACCESS"], creds["ACCESS_SECRET"])
api = tweepy.API(auth, wait_on_rate_limit=True)

start_date = datetime.fromisoformat(config["start_date"])
my_id_str = api.verify_credentials().id_str
responded_to = []

for dm in tweepy.Cursor(api.get_direct_messages, count=50).items():
    created_ts = int(dm.created_timestamp) / 1000 # twitter timestamps use milliseconds
    created = datetime.fromtimestamp(created_ts, tz=timezone.utc)

    if created < start_date: # hit the time limit
        break
    if dm.message_create["sender_id"] == my_id_str: # found a response from me
        break

    sender_id = dm.message_create["sender_id"]
    if sender_id in responded_to: # already responded to this person recently
        continue

    # useful for debugging, but shouldn't let this get logged in a public place
    #   like a GitHub action...
    # print("sending message to", sender_id)
    api.send_direct_message(recipient_id=sender_id, text=config["message"])
    responded_to.append(sender_id)

