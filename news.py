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

import feedparser
import time

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

# URLs of the RSS feeds
rss_urls = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://bitcoinmagazine.com/.rss/full/",
    "https://news.bitcoin.com/feed/",
    "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
    "https://coinjournal.net/news/feed/",
    "https://cryptobriefing.com/feed/",
    "https://www.newsbtc.com/feed/",
    "https://www.bloomberg.com/professional/feed/"
]

# Dictionary to keep track of latest posts for each RSS feed
latest_posts = {url: None for url in rss_urls}

while True:
    for url in rss_urls:
        # Parse the RSS feed
        feed = feedparser.parse(url)

        # Get the latest post from the RSS feed
        latest_post = feed.entries[0]

        # Check if the latest post is different from the previous one
        if latest_post != latest_posts[url]:
            # Save the latest post as the new previous post
            latest_posts[url] = latest_post

            # Extract the title and link of the latest post
            title = latest_post.title
            link = latest_post.link

            # Send a notification or perform any other action
            info = f"[{title}]({link})\n\n{hash(url)}"
            print(f"New post in {url}: {title} ({link})")
            
            # Send the message to the chat
            client.send_message(chat, info)

    # Wait for some time before checking for new posts again
    time.sleep(60)

client.run_until_disconnected()
