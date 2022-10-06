# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID","18860540"))
	API_HASH = os.environ.get("API_HASH","22dd2ad1706199438ab3474e85c9afab")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","5355558998:AAFehbjIvbfZTubH8b_0XlBKlu17M0Se4PY")
	BOT_USERNAME = os.environ.get("BOT_USERNAME","mirroeleech10bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL","-1001777759879"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER","5123176772"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Test4:Test4@cluster0.w2gkj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001777759879")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS","1236848594").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS","-1007947838838").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	SHORTNER_API_LINK = os.environ.get("SHORTNER_API_LINK", None)
	SHORTNER_API = os.environ.get("SHORTNER_API", None)
	REMOVE_WORD = list(set(str(x) for x in os.environ.get("REMOVE_WORD","mkvCinemas.mkv Haafiz Chapter").split()))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files and text Store Bot!
Send me any file or text, I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files and test Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** "IDK😎"

🧑🏻‍💻 **Developer:** "Berojgaar 😂"

👥 **Support Group:** "not need 🤓"

📢 **Updates Channel:** "not need💀"
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** ☠️

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
