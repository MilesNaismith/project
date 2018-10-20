from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import core_shopping_list
from db import db_session, Product

url_list = [
    'https://www.auchan.ru/pokupki/eda/bakaleja/makarony.html?p=',
    'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/olivki.html?p=',
    'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/goroshek-konservirovanny.html?p=',
    'https://www.auchan.ru/pokupki/eda/voda-i-napitki/soki-nektary.html?p=',
    'https://www.auchan.ru/pokupki/eda/masla-sousy-zapravki/masla-rastitelnye/podsolnechnoe-maslo.html?p=',
    'https://www.auchan.ru/pokupki/eda/bakaleja/krupy-boby/ris.html?p=',
    'https://www.auchan.ru/pokupki/eda/masla-sousy-zapravki/ketchup-tomatnaya-pasta/klassicheskiy-ketchup.html?p=',
    'https://www.auchan.ru/pokupki/eda/kofe-chai-sahar/chay/chernyj-chaj.html?p=',
    'https://www.auchan.ru/pokupki/kosmetika/uhod-za-volosami/shampuni-bal-zamy-maski/bal-zam-dlja-volos.html?p=',
    'https://www.auchan.ru/pokupki/kosmetika/sredstva-lichnoj-gigieny.html?p=',
    'https://www.auchan.ru/pokupki/hoztovary/stirka-i-uhod-za-bel-em/sredstva-dlja-stirki.html?p=',
]
def auchan_parse(url, substitution):
    ### Внимание! Функция парсит только Первую страницу каждого урла ###
    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html)
    section = soup.find("div",{"class": "products__list"})
    articles = section.find_all("article",{"class": "products__item"})
    products =[]
    for article in articles:
        name_src = article.find("a",{"class":"products__item-link"})
        price_full = article.find("div",{"class":"products__item-current-price current-price"})
        price_src = price_full.find("span",{"class":"price-val"})
        name = name_src.text
        price = price_src.text
        for key in substitution:
            if name == key:
                products.append({
                'title': substitution[key],
                 'price': price
                               })                 
    return products

def main():
    change = core_shopping_list.substitution('auchan')
    product_list_auchan = []
    for url in url_list:
        for page in range(1,5):
            url_page = url + str(page)
            print(product_list_auchan)
        product_list_auchan.extend(auchan_parse(url, change))    
    for item in product_list_auchan:
        prod = Product.query.filter(Product.name==item['title']).first()
        try:
            prod.auchan_price = item['price']
        except:
            pass
    db_session.commit()

if __name__ == "__main__":   
    main()    