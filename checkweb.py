import time
from pyrogram import Client, filters
import requests

api_id =  "1025907"
api_hash = "452b0359b988148995f22ff0f4229750"
bot_token = "6352531369:AAGKxdhMEAWgc19oh1c_WtzFwL0ectSPujw"

app = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False



url = "https://jobs.dbe.com.et/" # The URL of the website to check
chat_id = "399044004" # The chat_id to send the message to
interval = 10 * 120 # every 20 min



async def main():
    async with app:
        while True:
            if check_website(url):
                await app.send_message(chat_id, f"The website {url} is available!")
            time.sleep(interval)




app.run(main())