import asyncio
import os

import aiogram.types
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from flask import Flask, request
from flask_sslify import SSLify
BOT_TOKEN = "5468584401:AAHFgWlNuZEalDjX3pePvvbh6JySNiembIs"
APP_URL = f'https://f1cards.herokuapp.com/{BOT_TOKEN}'
admin_id = "787329642"
server = Flask(__name__)
loop = asyncio.get_event_loop()
storage = MemoryStorage()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=storage)
dp.middleware.setup(LoggingMiddleware())


@server.route('/' + BOT_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = aiogram.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == "__main__":
    from aiogram import executor
    from main import dp
    from admin import dp
    from cards_inf import dp
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    executor.start_polling(dp)