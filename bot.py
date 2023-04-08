import os
import telebot
import schedule
from time import sleep
from dotenv import load_dotenv
from parser_data import post_search

load_dotenv()

token = os.environ.get("TOKEN")
channel_id = "@IT_information_Lasto"
bot = telebot.TeleBot(token)
last_post = ""


def check_posts():
    global last_post
    last_post = post_search(last_post, bot, channel_id)


def start_bot():
    schedule.every(30).seconds.do(check_posts)
    while True:
        schedule.run_pending()
        sleep(1)



