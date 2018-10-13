import buttons
import csv
from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import auchan_parcer
import metro_parser
import perekrestok_parser
from db import db_session, Product

item_name = input('Что вы хотите добавить? Напишите название: ')
item_category = input('К какой категории товаров он относится?(видно пользователю) Напишите название: ')
item_url_auchan = input('Где искать этот товар на сайте Ашана? Напишите url: ')
item_name_auchan = input('Как продукт называет в Ашане? Напишите название: ')
item_url_metro = input('Где искать этот товар на сайте Metro? Напишите url: ')
item_name_metro = input('Как продукт называет в Metro? Напишите название: ')
item_url_perekrestok = input('Где искать этот товар на сайте Перекрестка? Напишите url: ')
item_name_perekrestok = input('Как продукт называет в Перекрестке? Напишите название: ')

def add_item():
    if item_category not in buttons.category_simple_list:
        item_category_buttons = input('Как назовем список с названием категории?(внутренне название) Напишите название: ')
        print ('OK! Тебе нужно будет самому создать в файле buttons.py list с этим именем, все оствльное создам автоматом!')
        buttons.category_simple_list.extend(item_category)
        buttons.category[item_category] = item_category_buttons
    try:
        buttons.item_category_buttons.append(InlineKeyboardButton(item_name, callback_data = item_name)
    except:
        print('ну я же говорил, создай List!')   
    with open('auchan_replace.csv', 'a', encoding='utf-8') as f:
        fields =['name_old', 'name_new']
        writer = csv.DictWriter(f, fields, delimiter =';')
        for row in writer:
            writer.writerow(item_name_auchan,item_name)
    with open('metro_replace.csv', 'a', encoding='utf-8') as f:
        fields =['name_old', 'name_new']
        writer = csv.DictWriter(f, fields, delimiter =';')
        for row in writer:
            writer.writerow(item_name_metro,item_name)
    with open('perekrestok_replace.csv', 'a', encoding='utf-8') as f:
        fields =['name_old', 'name_new']
        writer = csv.DictWriter(f, fields, delimiter =';')
        for row in writer:
            writer.writerow(item_name_perekrestok,item_name)                
    auchan_parcer.url_list.append(item_url_auchan)
    metro_parser.url_list.append(item_url_metro)
    perekrestok_parser.url_list.append(item_url_perekrestok)
    prod = Product(name = item_name)
    db_session.add(prod)
    db_session.commit()
    print ('OK! ')
if item_name not in buttons.item_list:
    buttons.item_list.extend(item_name)
    add_item()
else:
    print('Товар уже существует')
            