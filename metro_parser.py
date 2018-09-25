from bs4 import BeautifulSoup
from selenium import webdriver

def metro_parse(url,substitution=dict()):
    ### Внимание! Функция парсит только Первую страницу каждого урла ###
    browser = webdriver.PhantomJS()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html)
    section = soup.find("div",{"class": "items"})
    #articles = section.find_all("div",{"class": "catalog-i"})
    articles = section.find_all("div",{"class":("catalog-i","__price-rules")})
    print(articles)
    products =[]
    print(len(articles))
    c = 1
    for article in articles:
        name_src = article.find("span",{"class":"title"})
        art = article.find("span",{"class":"article"})
        
        print(c, name_src.text, art)
        c += 1
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
change = {#'Вермишель MAKFA длинная спагетти, 500г': 'Спагетти Макфа',
          #'Макароны MAKFA перья любительские, 450г': 'Макароны Макфа',
          #'Оливки MAESTRO DE OLIVA без косточек, 300г':'Оливки зеленые',
          #'Оливки MAESTRO DE OLIVA супергигантские без косточек, 420г' : 'Оливки черные',
          #'Зеленый горошек BONDUELLE Нежный, 400 г': 'Горошек',
          #'Кукуруза GLOBUS, 425мл':'Кукуруза',
          #'Сок ДОБРЫЙ Яблоко, 2л': 'Яблочный сок',
          'Сок SANTAL красный гранат, 1л':'Гранатовый сок'
           }    

url_list =[#'https://msk.metro-cc.ru/category/produkty/bakaleya/makaronnye-izdeliya?price_range=11%3B1361&brands=&attrs=&sorting=0&limit=72&in_stock=0&virtual_stock=0',
           #'https://msk.metro-cc.ru/category/produkty/ovoschi-griby/101009003-konservirovannye/?price_range=27%3B3397&brands=&attrs=&attr%5B253%5D%5Bfrom%5D=0&attr%5B253%5D%5Bto%5D=0&sorting=0&limit=72&in_stock=0&virtual_stock=0',
           'https://msk.metro-cc.ru/category/produkty/holodnye-napitki/soki-morsy-nektary?price_range=18%3B80&price_from=60&price_to=80&brands=&attrs=&attr%5B181%5D%5Bfrom%5D=0&attr%5B181%5D%5Bto%5D=0&sorting=0&limit=72&in_stock=0&virtual_stock=0',   
          ]
product_list =[]
for url in url_list:
    product_list += metro_parse(url,change)         
print(product_list)    