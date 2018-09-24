from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import pyautogui
from settings import PASSWORD, API_TOKEN, ID_CHAT

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def insertion(bot,update):
    user_text = update.message.text.split()
    user_text = ''.join(user_text)
    user_list = user_text.split(',')
    get_minimal_check(user_list)

def get_minimal_check(shopping_list):
    pass

def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', 'insertion'))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

main()