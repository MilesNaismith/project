from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import core_shopping_list

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
        price = price_int_src.text + '.' + price_float_src.text
        for key in substitution:
            if name == key:
                products.append({
                'title': substitution[key],
                 'price': price
                               })                              
    return products                                 

def main():
    change = change = core_shopping_list.substitution('metro')
    url_list =['https://msk.metro-cc.ru/category/produkty/bakaleya/makaronnye-izdeliya?price_range=11%3B1361&brands=&in_stock=1&attrs=&sorting=0&limit=72&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/ovoschi-griby/101009003-konservirovannye?price_range=27%3B3397&brands=&in_stock=1&attrs=&attr%5B253%5D%5Bfrom%5D=0&attr%5B253%5D%5Bto%5D=0&sorting=0&limit=72&virtual_stock=0',
               'https://msk.metro-cc.ru/category/produkty/holodnye-napitki/soki-morsy-nektary?price_range=15%3B1693&brands=&in_stock=1&attrs=&attr%5B181%5D%5Bfrom%5D=0&attr%5B181%5D%5Bto%5D=0&sorting=0&limit=72&virtual_stock=0',   
              ]
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
    with open('metro.csv','w', encoding='utf-8') as f:
        fields = ['title', 'price']
        writer =csv.DictWriter(f,fields,delimiter =';')
        for item in product_list_metro:
            writer.writerow(item)
    
if __name__ == "__main__":
    main()