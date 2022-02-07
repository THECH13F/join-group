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
Starting_group=os.environ.get("Starting_group", False)
api_hash=os.environ.get("API_HASH", False)
api_id=os.environ.get("API_ID", False)
string =os.environ.get("SESSION", False)
async def main():
    async with TelegramClient(StringSession(string), api_id, api_hash) as client:
        await client.start()
        to_the1="https://pastebin.com/raw/1kvXvHAe"
        sendto1=requests.get(to_the1).text.split('\n')
        joined=tme=failed=0
        message = await client.send_message("me", 'Starting joining group!!')
        for i in range(int(Starting_group),len(sendto1),1):
            try:
                await client(JoinChannelRequest(sendto1[i]))
                joined+=1
                print(f'CHANNEL JOINED {sendto1[i]}')
                await client.edit_message("me",message, f'**Group/CHANNEL joining by CHIEF**\nCHANNEL/GROUP JOINNED `{sendto1[i]}` \njoined:- {joined}\nerror:- {failed}')
                time.sleep(240)
            except FloodWaitError as fwe:
                print(f'Waiting for {fwe}')
                await client.edit_message("me",message, f'**Group/CHANNEL joining by CHIEF**\nWAITING FOR {fwe} Seconds\njoined:- {joined}\nerror:- {failed}')
                try:
                    tme = int(fwe.seconds)
                    day = tme // (24 * 3600)
                    tme = tme % (24 * 3600)
                    hour = tme // 3600
                    tme %= 3600
                    minutes = tme // 60
                    tme %= 60
                    seconds = tme
                    print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
                    await client.send_message("me",message=f"**Group/CHANNEL joining by CHIEF**\nyour total waiting time is for\nd:h:m:s-> {int(day)}:{int(hour)}:{int(minutes)}:{int(seconds)}")
                    await asyncio.sleep(delay=fwe.seconds)
                except:
                    await asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
                print(f"Encountered an error while joining {sendto1[i]}\n{err}")
                failed+=1
                await client.edit_message("me",message, f'**Group/CHANNEL joining by CHIEF**\nEncountered an error while joining `{sendto1[i]}`\nerror:-{err}\njoined:- {joined}\nerror:- {failed}')
        else:
            print("ALL GROUP JOINING COMPLETE!!")
            await client.send_message("me",message=f"**Group/CHANNEL joining by CHIEF**\nALL GROUP JOINING IS COMPLETED")
              

asyncio.run(main())
f.close()
