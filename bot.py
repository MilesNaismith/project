from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from settings import API_TOKEN, YA_API_KEY, PROXY
import core_shopping_list
import buttons
import codecs
import copy
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
    print(user_data.get('button_list'))
    user_data['category_list'] = copy.deepcopy(buttons.category_list)
    user_data['category'] = copy.deepcopy(buttons.category)
    button_list = user_data['category_list']
    reply_markup = InlineKeyboardMarkup(build_menu(
        button_list,
        n_cols=len(button_list)//2), 
        footer_buttons = buttons.footer_buttons_done
    )
    message_text = 'выбирайте продукты'
    bot.send_message(
        chat_id = update.message.chat_id,
        message_id = update.message.message_id,
        text=message_text, 
        reply_markup=reply_markup
    )

def callbackHandler(bot, update, user_data):
    user_data.setdefault('shopping_list',[])
    if update.callback_query.data in buttons.category_simple_list:
        button_list = user_data['category'][update.callback_query.data]
        user_data['button_list'] = button_list 
        reply_markup = InlineKeyboardMarkup(build_menu(
            button_list, 
            n_cols=len(button_list)//2,
            footer_buttons = buttons.footer_buttons_back
        ))
        message_text = 'выбирайте продукты'
        bot.edit_message_text(
            chat_id=update.callback_query.message.chat.id, 
            message_id=update.callback_query.message.message_id, 
            text=message_text, 
            reply_markup=reply_markup, 
            parse_mode='HTML'
        )
    elif update.callback_query.data == 'Назад':
        button_list = user_data['category_list']
        reply_markup = InlineKeyboardMarkup(build_menu(
            button_list, 
            n_cols=len(button_list)//2,
            footer_buttons = buttons.footer_buttons_done
        ))
        message_text = 'выбирайте продукты'
        bot.edit_message_text(
            chat_id=update.callback_query.message.chat.id, 
            message_id=update.callback_query.message.message_id, 
            text=message_text, 
            reply_markup=reply_markup, 
            parse_mode='HTML'
        )
    elif update.callback_query.data != 'Готово':
        button_list = user_data['button_list']
        for button in button_list:
            if button.callback_data == update.callback_query.data:
                if button.text.endswith('✔'):
                    button.text = update.callback_query.data   
                    user_data['shopping_list'].remove(update.callback_query.data)
                else:
                    button.text = '{} ✔'.format(update.callback_query.data)
                    user_data['shopping_list'].append(update.callback_query.data)
            
        reply_markup = InlineKeyboardMarkup(build_menu(
            button_list, 
            n_cols=len(button_list)//2,
            footer_buttons = buttons.footer_buttons_back
        ))
        message_text = 'выбирайте продукты'
        bot.edit_message_text(
            chat_id=update.callback_query.message.chat.id, 
            message_id=update.callback_query.message.message_id, 
            text=message_text, 
            reply_markup=reply_markup, 
            parse_mode='HTML'
        )         
    elif update.callback_query.data == 'Готово':
        check = core_shopping_list.main(user_data['shopping_list'])
        shopping_string = ', '.join(user_data['shopping_list']) + '\n'
        try:
            text ='Список покупок: \n{}Стоимость покупок \nВ Ашане {}\nВ Metro {}\nВ Перекрестке {}'.format(
                shopping_string,
                check[0][1],check[1][1],
                check[2][1]
            ) 
            user_data['shopping_list'] = []
            user_data['min_shop']= check[-1]
            if user_data['min_shop'] == 'Auchan':
                user_data['min_shop'] = 'Ашан'
            elif user_data['min_shop'] == 'Metro':
                user_data['min_shop'] = 'Metro Cash & Carry'        
            elif user_data['min_shop'] == 'Perekrestok':
                user_data['min_shop'] = 'Перекресток' 
            update.callback_query.message.reply_text(text=text) 
            geolocation(bot, update,user_data)
            user_data = None
        except Exception as e:
            text = 'Данный товар отсутствует во всех магазинах' 
            update.callback_query.message.reply_text(text=text) 

def geolocation(bot, update,user_data):
    accept_keyboard = telegram.KeyboardButton(text='Показать', request_location=True)
    decline_keyboard = telegram.KeyboardButton(text='Не показывать')
    custom_keyboard = [[ accept_keyboard, decline_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,one_time_keyboard=True,resize_keyboard=True)
    text='Показать ближайшие магазины сети {}?'.format(user_data['min_shop'])
    update.callback_query.message.reply_text(text=text, reply_markup=reply_markup) 

def location(bot, update, user_data):
    coord = (float(update.message.location.latitude), float(update.message.location.longitude))
    user_data['coord'] = '{},{}'.format(coord[1],coord[0])
    shop_map= core_shopping_list.ya_api(user_data['min_shop'],user_data['coord'],YA_API_KEY)
    bot.send_photo(chat_id=update.message.chat_id, photo=shop_map)

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