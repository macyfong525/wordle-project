#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
from wordle import Wordle

from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# config
TOKEN_FILE = "config.json"
wordle = Wordle()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    button = InlineKeyboardMarkup([[InlineKeyboardButton('wordle', url='https://www.nytimes.com/games/wordle/index.html')]])
    update.message.reply_text(wordle.start(), reply_markup=button)


def help(update, context):
    """Send a message when the command /help is issued."""
    help_message = "/start pick one word for wordle\n/input <word> <status> example: raise ybbgg"
    update.message.reply_text(help_message)


def input(update, context):
    """
    context: <word> <status>
    """
    logger.info(update.message.text)
    word = update.message.text.split(" ")[1]
    status = update.message.text.split(" ")[2]
    wordle.insert(word, status)
    update.message.reply_text(wordle.get_suggested_words())


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(json.load(open(TOKEN_FILE))["TOKEN"], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("input", input))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()