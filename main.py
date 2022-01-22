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
group=os.environ.get("GROUP_ID", False)
api_hash=os.environ.get("API_HASH", False)
api_id=os.environ.get("API_ID", False)
string =os.environ.get("SESSION", False)
async def main():
    async with TelegramClient(StringSession(string), api_id, api_hash) as client:
        await client.start()
        to_the1="https://pastebin.com/raw/1kvXvHAe"
        sendto1=requests.get(to_the1).text.split('\n')
        for i in range(0,len(sendto1),1):
            receiver=client.get_entity(group)
            try:
                await client(JoinChannelRequest(sendto1[i]))
                print(f'CHANNEL JOINED {sendto1[i]}')
                await client.send_message(entity=receiver,message=f'CHANNEL JOINNED {sendto1[i]}')
                time.sleep(150)
            except FloodWaitError as fwe:
                print(f'Waiting for {fwe}')
                await client.send_message(entity=receiver,message=f'WAITING FOR {fwe}')
                await asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
                print(f"Encountered an error while joining {sendto1[i]}\n{err}")
                await client.send_message(entity=receiver,message=f"Encountered an error while joining {sendto1[i]}\n{err}")

asyncio.run(main())
f.close()
