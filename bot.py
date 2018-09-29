from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import telegram
#from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from settings import API_TOKEN
import get_price

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



def insertion(bot, update):
    product_list = ['Кукуруза', 'Яблочный сок', 'Горошек', 'Макароны Макфа', 'Спагетти Макфа']
    shopping_list = update.message.text[7:].split(',')
    shopping_list = [x.strip() for x in shopping_list]
    for item in shopping_list:
        if not item in product_list:
            text = item + ' не найден в базе, попробуйте заменить товар на аналогичный или написать более общее название'
            update.message.reply_text(text)
    print('обработал список')
    text = get_price.main(shopping_list)
    print('вывод результата')
    update.message.reply_text(text)
            


def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', insertion))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 
if __name__ == "__main__":
    main()