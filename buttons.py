from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import buttons

water_list = [
    InlineKeyboardButton('Яблочный сок', callback_data = 'Яблочный сок'),
    InlineKeyboardButton('Гранатовый сок', callback_data = 'Гранатовый сок'),
    InlineKeyboardButton('Назад', callback_data = 'Назад')
]

canned_food_list = [
    InlineKeyboardButton('Оливки', callback_data = 'Оливки'),
    InlineKeyboardButton('Маслины', callback_data = 'Маслины'),
    InlineKeyboardButton('Кукуруза', callback_data = 'Кукуруза'),
    InlineKeyboardButton('Горошек', callback_data = 'Горошек'),
    InlineKeyboardButton('Назад', callback_data = 'Назад')
]

pasta_list = [
    InlineKeyboardButton('Макароны Макфа', callback_data = 'Макароны Макфа'),
    InlineKeyboardButton('Спагетти Макфа', callback_data = 'Спагетти Макфа'),
    InlineKeyboardButton('Назад', callback_data = 'Назад')    
]

category_list = [
    InlineKeyboardButton('Соки', callback_data = 'Соки'),
    InlineKeyboardButton('Консервы', callback_data = 'Консервы'),
    InlineKeyboardButton('Бакалея', callback_data = 'Бакалея'),
    InlineKeyboardButton('Готово', callback_data = 'Готово')    
]

category = {
    'Соки' : buttons.water_list,
    'Консервы' : buttons.canned_food_list,
    'Бакалея' : buttons.pasta_list 
}

category_list1 = ['Соки','Консервы','Бакалея']
