from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from settings import API_TOKEN,ya_api_key,PROXY
import core_shopping_list
#import requests

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu    

def table(bot, update, user_data):
    print(update)  
    user_data['shopping_list'] = []
    user_data['ID_CHAT'] = update.message.chat_id
    button_list = [ 
        InlineKeyboardButton('Кукуруза', callback_data = 'Кукуруза'),
        InlineKeyboardButton('Горошек', callback_data = 'Горошек'),
        InlineKeyboardButton('Оливки', callback_data = 'Оливки'),
        InlineKeyboardButton('Маслины', callback_data = 'Маслины'),
        InlineKeyboardButton('Макароны Макфа', callback_data = 'Макароны Макфа'),
        InlineKeyboardButton('Спагетти Макфа', callback_data = 'Спагетти Макфа'),
        InlineKeyboardButton('Яблочный сок', callback_data = 'Яблочный сок'),
        InlineKeyboardButton('Гранатовый сок', callback_data = 'Гранатовый сок'),
        InlineKeyboardButton('Готово', callback_data = 'Готово')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=len(button_list)//4,))
    message_text = 'выбирайте продукты'
    bot.send_message(chat_id=user_data['ID_CHAT'], text=message_text, reply_markup=reply_markup, parse_mode='HTML')

def callbackHandler(bot, update, user_data):    
    user_data.setdefault('ID_CHAT',update['callback_query']['message']['chat']['id'])
    user_data.setdefault('shopping_list',[])
    if update.callback_query.data != 'Готово':
        user_data['shopping_list'].append(update.callback_query.data)
        update.callback_query.inline_message_id = 1
        print(update.callback_query.inline_message_id)
        #editMessageText(inline_message_id=update.callback_query.inline_message_id, text='{}✓'.format(update.callback_query.data))
        print(user_data['shopping_list']) 
    else:
        check = core_shopping_list.main(user_data['shopping_list'])
        print(check)
        shopping_string = core_shopping_list.list_to_string(user_data['shopping_list'])
        text ='Список покупок: {} \nВ Ашане покупки по данному списку обойдутся в {}, в Metro цена составит {}, а в перекрестке {}'.format(shopping_string,check[0][1],check[1][1], check[2][1])
        user_data['shopping_list'] = []
        user_data['min_shop']= check[-1]
        if user_data['min_shop'] == 'Auchan':
            user_data['min_shop'] = 'Ашан'
        elif user_data['min_shop'] == 'Metro':
            user_data['min_shop'] = 'Metro Cash & Carry'        
        elif user_data['min_shop'] == 'Perekrestok':
            user_data['min_shop'] = 'Перекресток'  
        bot.send_message(chat_id=user_data['ID_CHAT'], text=text)
        geolocation(bot, update,user_data)

def geolocation(bot, update,user_data):
    accept_keyboard = telegram.KeyboardButton(text='Показать', request_location=True)
    decline_keyboard = telegram.KeyboardButton(text='Не показывать')
    custom_keyboard = [[ accept_keyboard, decline_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True,resize_keyboard=True)
    bot.send_message(chat_id=user_data['ID_CHAT'], 
                     text='Показать ближайшие магазины сети {}?'.format(user_data['min_shop']), 
                     reply_markup=reply_markup)

def location(bot, update, user_data):
    coord = (float(update.message.location.latitude), float(update.message.location.longitude))
    user_data['coord'] = '{},{}'.format(coord[1],coord[0])
    print('магазин из location',user_data['min_shop'])
    shop_map= core_shopping_list.ya_api(user_data['min_shop'],user_data['coord'],ya_api_key)
    bot.send_photo(chat_id=user_data['ID_CHAT'], photo=shop_map)

def main():
    mybot = Updater(API_TOKEN, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', table, pass_user_data=True))
    dp.add_handler(CommandHandler('geo', geolocation,pass_user_data=True))
    dp.add_handler(CallbackQueryHandler(callbackHandler, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, location, pass_user_data=True))
    #Начало цикла
    mybot.start_polling()
    mybot.idle()
 
if __name__ == "__main__":
    main()