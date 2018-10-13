from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import buttons

footer_buttons_back = [
    InlineKeyboardButton('**Назад**', callback_data = 'Назад')
]

footer_buttons_done = [
    InlineKeyboardButton('**Готово**', callback_data = 'Готово')    
]
water_list = [
    InlineKeyboardButton('Яблочный сок', callback_data = 'Яблочный сок'),
    InlineKeyboardButton('Гранатовый сок', callback_data = 'Гранатовый сок'),
]

canned_food_list = [
    InlineKeyboardButton('Оливки', callback_data = 'Оливки'),
    InlineKeyboardButton('Маслины', callback_data = 'Маслины'),
    InlineKeyboardButton('Кукуруза', callback_data = 'Кукуруза'),
    InlineKeyboardButton('Горошек', callback_data = 'Горошек'),
]

pasta_list = [
    InlineKeyboardButton('Макароны Макфа', callback_data = 'Макароны Макфа'),
    InlineKeyboardButton('Спагетти Макфа', callback_data = 'Спагетти Макфа'),
]

category_list = [
    InlineKeyboardButton('Соки', callback_data = 'Соки'),
    InlineKeyboardButton('Консервы', callback_data = 'Консервы'),
    InlineKeyboardButton('Бакалея', callback_data = 'Бакалея'),
]

category = {
    'Соки' : buttons.water_list,
    'Консервы' : buttons.canned_food_list,
    'Бакалея' : buttons.pasta_list 
}

category_simple_list = ['Соки','Консервы','Бакалея']

item_list = [
    'Макароны Макфа',
    'Спагетти Макфа',
    'Маслины',
    'Оливки',
    'Горошек',
    'Кукуруза',
    'Яблочный сок',
    'Гранатовый сок',
 ]