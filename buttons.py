from telegram import InlineKeyboardButton

footer_buttons_back = [
    InlineKeyboardButton('**Назад**', callback_data = 'Назад')
]

footer_buttons_done = [
    InlineKeyboardButton('**Готово**', callback_data = 'Готово')    
]

household =[
    InlineKeyboardButton('Гель для стирки', callback_data = 'Гель для стирки'),
    InlineKeyboardButton('Туалетная бумага', callback_data = 'Туалетная бумага'),
    InlineKeyboardButton('Шампунь', callback_data = 'Шампунь'),
]

water_list = [
    InlineKeyboardButton('Яблочный сок', callback_data = 'Яблочный сок'),
    InlineKeyboardButton('Гранатовый сок', callback_data = 'Гранатовый сок'),
    InlineKeyboardButton('Молоко', callback_data = 'Молоко'),
    InlineKeyboardButton('Чай', callback_data = 'Чай'),
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
    InlineKeyboardButton('Готовое тесто', callback_data = 'Готовое тесто'),
    InlineKeyboardButton('Масло подсолнечное', callback_data = 'Масло подсолнечное'),
    InlineKeyboardButton('Масло сливочное', callback_data = 'Масло сливочное'),
]

category_list = [
    InlineKeyboardButton('Напитки', callback_data = 'Напитки'),
    InlineKeyboardButton('Консервы', callback_data = 'Консервы'),
    InlineKeyboardButton('Бакалея', callback_data = 'Бакалея'),
    InlineKeyboardButton('Хозтовары', callback_data = 'Хозтовары'),
]

category = {
    'Напитки' : water_list,
    'Консервы' : canned_food_list,
    'Бакалея' : pasta_list,
    'Хозтовары': household,
}

category_simple_list = ['Напитки', 'Консервы', 'Бакалея', 'Хозтовары']

item_list = [
    'Макароны Макфа',
    'Спагетти Макфа',
    'Маслины',
    'Оливки',
    'Горошек',
    'Кукуруза',
    'Яблочный сок',
    'Гранатовый сок',
    'Готовое тесто',
    'Молоко',
    'Масло сливочное',
    'Масло подсолнечное',
    'Рис',
    'Кетчуп',
    'Чай',
    'Шампунь',
    'Гель для стирки',
    'Туалетная бумага',
 ]