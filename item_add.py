import buttons
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import auchan_parcer
import metro_parser
import perekrestok_parser
from db import db_session, Product

item_name = input('Что вы хот ите добавить?')
item_category = input('К какой категории товаров он относится?(видно пользователю)')
item_url_auchan = input('Где искать этот товар на сайте Ашана?')
item_url_metro = input('Где искать этот товар на сайте Metro?')
item_url_perekrestok = input('Где искать этот товар на сайте Перекрестка?')

def add_item():
    if item_category not in buttons.category_simple_list:
        buttons.category_simple_list.extend(item_category)
        item_category_buttons = input('Как назовем список с названием категории?(внутренне название)')
    item_category_buttons.append(InlineKeyboardButton(item_name, callback_data = item_name))    
    auchan_parcer.url_list.append(item_url_auchan)
    metro_parser.url_list.append(item_url_metro)
    perekrestok_parser.url_list.append(item_url_perekrestok)
    Product(name = item_name)
    db_session.add(prod)
    db_session.commit()
if item_name not in buttons.item_list:
    buttons.item_list.extend(item_name)
    add_item()
else:
    print('Товар уже существует')
            