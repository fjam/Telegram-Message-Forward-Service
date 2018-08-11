import asyncio
from telethon import TelegramClient, events

api_id = 
api_hash = ''

client = TelegramClient('session_id', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def my_event_handler(event):
    print(event)
    if '1113462530' in str(event):
        await client.send_message('tbtradinggroup', event.raw_text)
 
client.run_until_disconnected()