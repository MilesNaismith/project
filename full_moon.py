''' Полнолуние
Научить бота отвечать на вопрос “Когда ближайшее полнолуние после 2016-10-01?”. 
Чтобы узнать, когда ближайшее полнолуние, используй модуль ephem. Чтобы им пользоваться, 
его нужно установить ($ pip install ephem) и импортировать. '''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from settings import API_TOKEN, ID_CHAT
import ephem
from datetime import datetime, date, time
import telegram

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def full_moon(bot,update):
    user_text = update.message.text.split()
    user_date = user_text[-1]
    try:
        date_dt = datetime.strptime(user_date, '%d.%m.%Y')
    except (TypeError, ValueError):
        text ='Введите дату в формате дд.мм.гггг'
        print(text)    
        update.message.reply_text(text)        
    text = ephem.next_full_moon(date_dt)    
    print(text)
    update.message.reply_text(text)



def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('fullmoon', full_moon))
    mybot.start_polling()
    mybot.idle()
 
if __name__ == "__main__":
    main()