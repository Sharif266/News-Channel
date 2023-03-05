import asyncio
import json
import logging
import math
import os
import random
import re
import sys
from time import sleep
import feedparser
import time
from random import choice, randrange, shuffle
from telethon.sync import TelegramClient
import requests
import telethon
from bs4 import BeautifulSoup
from telethon import TelegramClient, events, functions, sync, types
from telethon.errors import (FloodWaitError, MessageAuthorRequiredError,
                             SessionPasswordNeededError,
                             UserAlreadyParticipantError)
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import (EditMessageRequest,
                                            GetBotCallbackAnswerRequest,
                                            GetHistoryRequest,
                                            GetMessageEditDataRequest,
                                            ImportChatInviteRequest)
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputMessagesFilterVideo

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)
import urllib.request
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import stripe
import traceback
from traceback import format_exc
from colorama import Fore, init as color_ama
color_ama(autoreset=True)
cend = Fore.RESET

if not os.path.exists("session"):
    os.makedirs("session")

api_id = 1752232
api_hash = 'b693218784e03bd05bdca73a04fd8999'
bot_api = "5716134117:AAFr0gqGngnSDfOmRYQhRwku8Xgg0DFUDVc"

client = TelegramClient("session/bot1", api_id, api_hash)
client.start(bot_token=bot_api)
if client.is_user_authorized():
    print ("The bot is alive")
else:
    client.disconnect()
    os.system('exit')

def hash(url):
	if "coindesk" in url:
		return "#coindesk"
	elif "cointelegraph" in url:
		return "#cointelegraph"
	elif "bitcoinmagazine" in url:
		return "#bitcoinmagazine"
	elif "bitcoin" in url:
		return "#newsbitcoin"
	elif "reutersagency" in url:
		return "#reutersagency"
	elif "coinjournal" in url:
		return "#coinjournal"
	elif "cryptobriefing" in url:
		return "#cryptobriefing"
	elif "newsbtc" in url:
		return "#newsbtc"
	elif "bloomberg" in url:
		return "#bloomberg"

urls = ("https://www.coindesk.com/arc/outboundfeeds/rss/",
	"https://cointelegraph.com/rss",
	"https://bitcoinmagazine.com/.rss/full/",
	"https://news.bitcoin.com/feed/",
	"https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
	"https://coinjournal.net/news/feed/",
	"https://cryptobriefing.com/feed/",
	"https://www.newsbtc.com/feed/",
	"https://www.bloomberg.com/professional/feed/"
	)

chat = "https://t.me/NewsBo_X"


latest_posts = {}

while True:
    for url in urls:
        feed = feedparser.parse(url)
        latest_post = feed.entries[0]
        sleep(0.1)
        info = ''
        title = "[{}]({})".format(latest_post.title,latest_post.link)
        info += title+"\n\n{}".format(hash(url))
        # Check if the latest post for this URL is different from the last sent post
        if url in latest_posts and latest_posts[url] == latest_post:
            print("Skipping duplicate post for URL:", url)
        else:
            # Send the message to the chat and update the latest post for this URL
            client.send_message(chat, info)
            latest_posts[url] = latest_post
            print("Sent new post for URL:", url)

    sleep (5*60)
'''
while True:
	for url in urls:
		feed = feedparser.parse(url)
		latest_post = feed.entries[0]
		sleep(0.1)
		info = ''
		title = "[{}]({})".format(latest_post.title,latest_post.link)
		info += title+"\n\n{}".format(hash(url))
		client.send_message(chat,info)
		print (Fore.RED+"==>>Message Send Done"+cend)
		sleep(0.5)
'''
client.run_until_disconnected()
