#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21887008", default=None, cast=int)
API_HASH = config("2d394dee98f44c1038d17ab7fdabe92f", default=None)
BOT_TOKEN = config("7639728457:AAFj1Wm_ASF7MA01aDWJZNEQwBgj1ygXGGM", default=None)
SESSION = config("BAFN-CAAuyjFHdmoNousc5BUX27tn5idcDKE2RBf-_exjcMqA_lQmIUsBTBEAOrka3z7vP78ZVlnolscFEgyeJl91rdZri27pV3o_KewJWZj8GpjyFzMC0txymyMKR4mK6k3BaP9cp-1Eg9T_H-BOozI3wsEcu1jc3Vf7rZyd2t_sJdCdwVXvAyO_UGW11NjA0HkzkdYJGd5p7pHlxBRReCpBQqgijQQJdsGXapa8AqY1he4X-zoKD3iD4wlJJzyWAm2jivxA2gWwQIoBt5yCKG4V3F-ymP409nNs2JRay9JzGK06p19q5bfjAoZK8hn4ylpEOMLkdPTyA7cPWusW4rfqdXx2QAAAAGOedYsAA", default=None)
FORCESUB = config("@freetiktok_views", default=None)
AUTH = config("6685316652", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
