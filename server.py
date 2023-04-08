from os import environ
from flask import Flask
from dotenv import load_dotenv
from bot import start_bot

load_dotenv()

app = Flask(__name__)


@app.route(f"{environ.get('URL')}")
def run_bot():
    start_bot()


app.run()
