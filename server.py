import os
import telebot
import schedule
from time import sleep
from dotenv import load_dotenv
from parser_data import post_search

load_dotenv()

token = os.environ.get("TOKEN")
channel_id = "@IT_information_Lasto"
admin_id = int(os.environ.get("ADMIN_ID"))
bot = telebot.TeleBot(token)
last_post = ""


def check_posts():
    global last_post
    last_post = post_search(last_post, bot, channel_id)


@bot.message_handler(commands=["start"])
def start_bot(message):
    user_id = message.from_user.id
    if user_id != admin_id:
        bot.send_message(message.from_user.id, "Вы не являетесь администратором")
    else:
        bot.send_message(message.from_user.id, "Бот запущен")
        schedule.every(1).hours.do(check_posts)
        while True:
            schedule.run_pending()
            sleep(1)


bot.polling()

