import json
import asyncio
import time
import os
import requests
import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.sessions import StringSession
f = open ('app.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating through the json
# list
group=data["env"]['GROUP_ID']['value']
api_hash=os.environ.get("API_HASH", False)
api_id=os.environ.get("API_ID", False)
#api_hash=data["env"]["API_HASH"]["value"]
string =os.environ.get("SESSION", False)
with TelegramClient(StringSession(string), api_id, api_hash) as client:
  client.start()
  to_the1="https://pastebin.com/raw/1kvXvHAe"
  sendto1=requests.get(to_the1).text.split('\n')
  for i in range(0,len(sendto1),1):
    receiver=client.get_entity(group)
    try:
        client(JoinChannelRequest(sendto1[i]))
        print(f'CHANNEL JOINED {sendto1[i]}')
        client.send_message(entity=receiver,message=f'CHANNEL JOINNED {sendto1[i]}')
        time.sleep(150)
    except FloodWaitError as fwe:
        print(f'Waiting for {fwe}')
        asyncio.sleep(delay=fwe.seconds)
        client.send_message(entity=receiver,message=f'WAITING FOR {fwe}')
    except Exception as err:
        print(f"Encountered an error while joining {sendto1[i]}\n{err}")
        client.send_message(entity=receiver,message=f"Encountered an error while joining {sendto1[i]}\n{err}")


f.close()
