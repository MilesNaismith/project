from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import core_shopping_list
from db import db_session, Product

url_list =['https://www.perekrestok.ru/catalog/makarony-krupy-spetsii/makaronnye-izdeliya?page=',
               'https://www.perekrestok.ru/catalog/konservy-orehi-sousy/ovoschnye-konservy?page=',
               'https://www.perekrestok.ru/catalog/soki-vody-napitki/soki-nektary?page=', 
               'https://www.perekrestok.ru/catalog/moloko-syr-yaytsa/slivochnoe-maslo-i-margarin?page=',
               'https://www.perekrestok.ru/catalog/moloko-syr-yaytsa/moloko?page=',
               'https://www.perekrestok.ru/catalog/makarony-krupy-spetsii/krupy-i-bobovye?page=',
               'https://www.perekrestok.ru/catalog/konservy-orehi-sousy/tomatnye-pasty-ketchup?page=',
               'https://www.perekrestok.ru/catalog/zamorojennye-produkty/polufabrikaty?page=',
               'https://www.perekrestok.ru/catalog/makarony-krupy-spetsii/maslo-rastitelnoe?page=',
               'https://www.perekrestok.ru/catalog/kofe-chay-sahar/chay?page=',
               'https://www.perekrestok.ru/catalog/krasota-gigiena-bytovaya-himiya/uhod-za-volosami/shampuni-i-sredstva-dlya-uhoda-posle-mytya?page=',
               'https://www.perekrestok.ru/catalog/krasota-gigiena-bytovaya-himiya/tualetnaya-bumaga?page=',
               'https://www.perekrestok.ru/catalog/krasota-gigiena-bytovaya-himiya/stirka-i-uhod-za-belem?page=',
              ]

def perekrestok_parse(url,substitution=dict()):
    ### Внимание! Функция парсит только Первую страницу каждого урла ###
    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html)
    section = soup.find("ul",{"class": "xf-catalog"})
    articles = section.find_all("li",{"class":"js-catalog-product"})
    products =[]
    for article in articles:
        name_src = article.find("a",{"class":"xf-product-title__link"})
        price_full = article.find("div",{"class":["xf-product__cost","xf-product-cost"]})
        if price_full is None:
            price = 'нет в наличии'
        else:
            try:    
                price_int_src = price_full.find("span",{"class":"xf-price__rouble"})
                price_float_src = price_full.find("span",{"class":"xf-price__penny"})
                price = price_int_src.text + '.' + price_float_src.text[price_float_src.text.find(',')+1:price_float_src.text.find(',')+3]
            except AttributeError:
                price = None    
        name = name_src.get('title')
        
        for key in substitution:
            if name == key:
                products.append({
                              'title': substitution[key],
                              'price': price
                                }) 
    return products                                 

def main():
    change = change = core_shopping_list.substitution('perekrestok')    
    product_list_perekrestok =[]
    for url in url_list:
        for page in range(1,20):
            url_page = url + str(page)
            product_list_perekrestok += perekrestok_parse(url_page,change)    
    temp=[]
    for item in product_list_perekrestok:
        if item not in temp:
            temp.append(item)
    product_list_perekrestok = temp
    for item in product_list_perekrestok:
        prod = Product.query.filter(Product.name==item['title']).first()
        try:
            prod.perekrestok_price = item['price']
        except AttributeError:
            pass    
    db_session.commit()
    

if __name__ == "__main__":
    main()