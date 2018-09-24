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

autorized=[]

def keyboard_off(bot, update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=ID_CHAT, text="I'm back.", reply_markup=reply_markup)               

def autorization(bot,update):
    global autorized
    d = update.effective_user
    if d.username in autorized:
        keyboard_opener(bot, update)
    else:
        user_text = update.message.text.split()
        if user_text[1] == PASSWORD:
            text = 'Авторизован'
            keyboard_opener(bot, update)
        else:
            text = 'Не авторизован, наберите /start пароль'        
    print(text)
    update.message.reply_text(text)
    print(autorized)

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def keyboard_opener(bot, update):
    reply_markup =  button_list = [InlineKeyboardButton('Открыть дверь', callback_data = '1')]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    message_text = 'Открыть дверь'
    bot.send_message(chat_id=ID_CHAT, text=message_text, reply_markup=reply_markup, parse_mode='HTML')
    
def callbackHandler(bot, update):
    user_id = update.callback_query.from_user.id
    user_name = update.callback_query.from_user.name
    if update.callback_query.data == '1':
        pyautogui.hotkey('ctrl','alt','f')
    else:
        print('Что-то пошло не так')    
         
def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CallbackQueryHandler(callbackHandler))
    dp.add_handler(CommandHandler('start', autorization))
    dp.add_handler(CommandHandler('open', keyboard_opener))
    dp.add_handler(CommandHandler('keyboard_off', keyboard_off))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 

main()