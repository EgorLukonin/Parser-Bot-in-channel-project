import os
import telebot
import schedule
from time import sleep
from dotenv import load_dotenv
from parser_data import post_search

load_dotenv()

token = os.environ.get("token")
channel_id = "@IT_information_Lasto"
bot = telebot.TeleBot(token)
last_post = ""


def check_posts():
    global last_post
    last_post = post_search(last_post, bot, channel_id)


schedule.every(3).hours.do(check_posts)
if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(1)


bot.polling()

