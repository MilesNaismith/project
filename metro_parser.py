from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import core_shopping_list
from db import db_session, Product

url_list =['https://msk.metro-cc.ru/category/produkty/bakaleya/makaronnye-izdeliya?price_range=11%3B1361&brands=&in_stock=1&attrs=&sorting=0&limit=72&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/ovoschi-griby/101009003-konservirovannye?price_range=27%3B3397&brands=&in_stock=1&attrs=&attr%5B253%5D%5Bfrom%5D=0&attr%5B253%5D%5Bto%5D=0&sorting=0&limit=72&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/holodnye-napitki/soki-morsy-nektary?price_range=15%3B1693&brands=&in_stock=1&attrs=&attr%5B181%5D%5Bfrom%5D=0&attr%5B181%5D%5Bto%5D=0&sorting=0&limit=72&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/sousy-pripravy/?price_range=14%3B2061&brands=&sorting=0&limit=72&in_stock=0&virtual_stock=0',  
               'https://msk.metro-cc.ru/category/produkty/molochnye/?price_range=8%3B4201&brands=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/hlebobulochnye-izdeliya/zamorozhennoe-testo-vypechka/?price_range=34%3B4916&brands=&attrs=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/napitki/paketirovannyj-chaj/?price_range=12%3B7849&brands=&attrs=&attr%5B4%5D%5Bfrom%5D=0&attr%5B4%5D%5Bto%5D=0&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/syrnye/?price_range=18%3B5961&brands=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/bakaleya/rastitelnoe-maslo/?price_range=54%3B13201&brands=&attrs=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/bakaleya/krupy/?price_range=13%3B1701&brands=&attrs=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
               'https://msk.metro-cc.ru/category/kosmetika-bytovaya-himiya/gigienicheskie-prinadlezhnosti/bumazhnye-vatnye-izdeliya/?price_range=8%3B3353&brands=&attrs=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
    ]

def metro_parse(url,substitution=dict()):
    ### Внимание! Функция парсит только Первую страницу каждого урла ###
    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html)
    section = soup.find("div",{"class": "items"})
    articles = section.find_all("div",{"class":"catalog-i"})
    products =[]
    for article in articles:
        name_src = article.find("span",{"class":"title"})
        art = article.find("span",{"class":"article"})
        price_full = article.find("div",{"price_cnt"})
        price_int_src = price_full.find("span",{"class":"int"})
        price_float_src = price_full.find("span",{"class":"float"})
        name = name_src.text
        try:
            price = price_int_src.text + '.' + price_float_src.text
        except AttributeError:
            price = None     
        for key in substitution:
            if name == key:
                products.append({
                'title': substitution[key],
                 'price': price
                               })                              
    return products                                 

def main():
    change = change = core_shopping_list.substitution('metro')
    product_list_metro =[]
    for url in url_list:
        for page in range(1,10):
            url_page = url+'&page='+ str(page)
            product_list_metro += metro_parse(url_page,change)         
    temp=[]
    for item in product_list_metro:
        if item not in temp:
            temp.append(item)
    product_list_metro = temp
    for item in product_list_metro:
        prod = Product.query.filter(Product.name==item['title']).first()
        try:
            prod.metro_price = item['price']
        except AttributeError:
            pass    
    db_session.commit()
    
if __name__ == "__main__":
    main()