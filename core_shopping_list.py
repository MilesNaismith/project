import csv
import requests
from db import db_session, Product

def get_check(shopping_list, shop):
    print('считаем чек в {}'.format(shop))
    check = 0
    for item in shopping_list:
        prod = Product.query.filter(Product.name==item).first() 
        try:
            if shop == 'Auchan':
                print(shopping_list)
                print(check)
                check += float(prod.auchan_price)
            elif shop == 'Metro':
                check += float(prod.metro_price)
            elif shop == 'Perekrestok':
                check += float(prod.perekrestok_price)
        except ValueError:
            return shop, 'часть товаров отсутствует в магазине'
    return shop, round(check, 2)

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

def ya_api(min_shop,my_coord,ya_api_key):
    url = 'https://search-maps.yandex.ru/v1/?text={}&type=biz&results=3&ll={}&lang=ru_RU&apikey={}'.format(min_shop,my_coord,ya_api_key)
    res  = requests.get(url)
    tabs = res.json()
    coord_list = []
    for item in tabs['features']:
        shop_coord = '{},{}'.format(item['geometry']['coordinates'][0],item['geometry']['coordinates'][1])
        coord_list.append(shop_coord)
    shop_coord_string =''
    for coord in coord_list:
        shop_coord_string +='~{},pm2gnm'.format(coord)
    print(shop_coord_string)    
    url = 'https://static-maps.yandex.ru/1.x/?ll={}&l=map&pt={},pm2blm{}'.format(my_coord,my_coord,shop_coord_string)
    print(url)
    res  = requests.get(url)
    return(url)
def get_min_check(check1, check2, check3):
    check_list = [check1, check2, check3]
    check_end_list= []
    for check in check_list:
        try:
            float(check)
            check_end_list.append(check)
        except:
            pass
    return min(check_end_list)

def main(shopping_list):
    print('запускаем основной скрипт')
    check_auchan = get_check(shopping_list, 'Auchan')
    check_metro = get_check(shopping_list, 'Metro')
    check_perekrestok = get_check(shopping_list, 'Perekrestok')
    min_check = get_min_check(check_auchan[1], check_metro[1], check_perekrestok[1])
    for value in [check_auchan, check_metro, check_perekrestok]:
        if min_check in value:
            min_shop = value[0]
    print('готовим результаты')
    return check_auchan, check_metro, check_perekrestok, min_shop


if __name__ == "__main__":
    pass
