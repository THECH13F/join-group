import json
import asyncio
from dotenv import load_dotenv
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
hash=data["env"]["API_HASH"]["value"]
api_id=data["env"]['API_ID']['value']
api_hash=data["env"]["API_HASH"]["value"]
string =data["env"]["SESSION"]["value"]
with TelegramClient(StringSession(string), api_id, api_hash) as client:
  '''client = TelegramClient(string,
                    api_id,
                    api_hash
                    )'''
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
