from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import core_shopping_list

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
            price_int_src = price_full.find("span",{"class":"xf-price__rouble"})
            price_float_src = price_full.find("span",{"class":"xf-price__penny"})
            price = price_int_src.text + '.' + price_float_src.text[price_float_src.text.find(',')+1:price_float_src.text.find(',')+3]
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

    url_list =['https://www.perekrestok.ru/catalog/makarony-krupy-spetsii/makaronnye-izdeliya?page=',
               'https://www.perekrestok.ru/catalog/konservy-orehi-sousy/ovoschnye-konservy?page=',
               'https://www.perekrestok.ru/catalog/soki-vody-napitki/soki-nektary?page=',   
              ]
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
    with open('perekrestok.csv','w', encoding='utf-8') as f:
        fields = ['title', 'price']
        writer =csv.DictWriter(f,fields,delimiter =';')
        writer.writeheader()
        for item in product_list_perekrestok:
            writer.writerow(item)
    return product_list_perekrestok

if __name__ == "__main__":
    main()