import csv
from db import db_session, Product
'''
###делает словарь с прайсом по одному магазину из name, не нужен при работе с БД###
def get_price(name):
    price_list =dict()
    file_name = name + '.csv'
    with open(file_name, 'r', encoding='utf-8') as f:
        fields = ['title','price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            price_list[row['title']] = row['price']
    return name, price_list     
'''
def get_check_auchan(shopping_list):
    print('считаем чек в ашане')
    check = 0
    for item in shopping_list:
        prod = Product.query.filter(Product.name==item).first()
        try:
            check += float(prod.auchan_price)
        except ValueError:
            return 'Metro', 'часть товаров отсутствует в магазине'
    return 'Auchan', round(check, 2)

def get_check_metro(shopping_list):
    print('считаем чек в metro')
    check = 0
    for item in shopping_list:
        prod = Product.query.filter(Product.name==item).first()
        try:
            check += float(prod.metro_price)
        except ValueError:
            return 'Metro', 'часть товаров отсутствует в магазине'    
    return 'Metro', round(check, 2)    

def get_check_perekrestok(shopping_list):
    print('считаем чек в перекрестке')
    check = 0
    for item in shopping_list:
        prod = Product.query.filter(Product.name==item).first()
        try:
            check += float(prod.perekrestok_price)
        except ValueError:
            return 'Metro', 'часть товаров отсутствует'
    return 'Perekrestok', round(check, 2)    
'''
###считает общий чек по одному магазину, при работе с БД надо переделать###
def get_check(shopping_list, price_list):
    check = 0
    for item in shopping_list:
        if item in price_list[1]:
            check += float(price_list[1][item])
    return price_list[0], round(check, 2)
'''
###Вытаскивам из .csv список продуктов, скоторыми умеем работать, оставлю так, ибо нагляднее###
def get_added_products():
    product_list = []
    with open('product_list.csv', 'r', encoding ='utf-8') as f:
        fields = ['title']
        reader = csv.reader(f, fields)
        for row in reader:
            product_list.append(row[0])
    return product_list

###приведение имен товаров разных магазинов к единому виду###
def substitution(name):
    file_name = name + '_replace.csv'
    product_list = dict()
    with open(file_name, 'r', encoding='utf-8') as f:
        fields =['name_old', 'name_new']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            product_list[row['name_old']] = row['name_new']
    return product_list     
'''
###основная считалка-собиралка###
def main(shopping_list):
    print('запускаем основной скрипт')
    price_list_auchan = get_price('auchan')
    price_list_metro = get_price('metro')
    price_list_perekrestok = get_price('perekrestok')
    check_auchan = get_check(shopping_list, price_list_auchan)
    check_metro = get_check(shopping_list, price_list_metro)
    check_perekrestok = get_check(shopping_list, price_list_perekrestok)
    print('готовим результаты')
    return check_auchan, check_metro, check_perekrestok
'''
def main(shopping_list):
    print('запускаем основной скрипт')
    check_auchan = get_check_auchan(shopping_list)
    check_metro = get_check_metro(shopping_list)
    check_perekrestok = get_check_perekrestok(shopping_list)
    print('готовим результаты')
    return check_auchan, check_metro, check_perekrestok


if __name__ == "__main__":
    pass
