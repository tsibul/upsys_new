#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
# https://t.me/Mafia_upsys_bot
import django
django.setup()
from game_management.models import *


import telebot
import configparser
import os
#cfg = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.cfg')
config = configparser.RawConfigParser()
config.read('config.cfg')
config_dict = dict(config.items('TG_BOT'))
api = config_dict['api']

API_TOKEN = api

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    loc = Location.objects.get(id=1)
    txt = loc.location_address
    bot.reply_to(message, txt)


bot.infinity_polling()