import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '7851526'))
API_HASH = environ.get('API_HASH', '93ba4db0ad662e558356871afe8ca6de')
BOT_TOKEN = environ.get('BOT_TOKEN', '7935496045:AAF4dyWSHhPn-0zVx7MeSpZHrGluJlo0oQk')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1491913883').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/Suriya_M2L')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002350694058'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001670136532 -1002070372480 -1001718739968 -1001765415450 -1001951551775 -1001898212023 -1002057398189').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://aftest:aftest@cluster0.rjlq1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb://mongo:96bc66f1499c1e61a7c3@lovetoride_mongodb:27017/?tls=false")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002350694058'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/wam.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001610274164').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002350694058'))
URL = environ.get('URL', 'https://switchle-auto3.zh4klt.easypanel.host/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002350694058'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How2Downloadz/4")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/How2Downloadz/4")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/How2Downloadz/4")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "663f446757423b12fcf5e4a49bfb75f0798d0f80")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "tnvalue.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "663f446757423b12fcf5e4a49bfb75f0798d0f80")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "tnvalue.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "663f446757423b12fcf5e4a49bfb75f0798d0f80")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "tnvalue.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "43200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "43200"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1001546131221')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001577428406'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
