#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "10811400")
API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6880015232:AAGgDfGzbhqVrrLM_WoQtMe5hdDHW4HYVIA")
ADMIN = int(os.environ.get("ADMIN", '5422016608'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Sunrises24BotUpdates")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "Sunrises24BotSupport")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Multi:Multi@cluster0.rj5ksvc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/cc7163490ce9ee2190514.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '542201660'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001832909090)
