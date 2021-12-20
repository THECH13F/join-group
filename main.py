# make sure to have telethon and python-dotenv installed
# create a file called .env in the current directory from where you are running the script
# put API_ID and  API_HASH in the .env file in the following format
# VARIABLE=VALUE


from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
import time

from dotenv import load_dotenv
import os
import asyncio

ID=int(input("enter your api_ID:-"))
Hash=input("enter your API_HASH:-")


with open("channels.txt") as file:
    CHANNELS = [ line.strip() for line in file.readlines() ]



async def main():
    async with TelegramClient('tg_session', ID, Hash) as client:
        for channel in CHANNELS:
            try:
                await client(JoinChannelRequest(channel))
                print(f"CHANNEL JOINED username:-{channel}")
                await client.send_message(channel,message=".addch")
                print(f"MESSAGE SENT TO {channel} SUCCESSFULL")

            except FloodWaitError as fwe:
                print(f'Waiting for {fwe}')
                await asyncio.sleep(delay=fwe.seconds)
            except Exception as err:
                print(f"Encountered an error while joining {channel}\n{err}")
            await asyncio.sleep(120)

asyncio.run(main())