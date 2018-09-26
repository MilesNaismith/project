from bs4 import BeautifulSoup
from selenium import webdriver

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
change = {'Макароны Makfa Спагетти 500г': 'Спагетти Макфа',
          'Макароны Makfa Перья 450г': 'Макароны Макфа',
          'Оливки Maestro de Oliva без косточки 300г':'Оливки зеленые',
          'Маслины Bonduelle Classique без косточки 300г' : 'Оливки черные',
          'Горошек 6 соток зеленый 400г': 'Горошек',
          'Кукуруза 6 Соток сладкая 340г':'Кукуруза',
          'Сок Добрый Яблочный 2л': 'Яблочный сок',
          'Сок Nar Гранатовый 1л':'Гранатовый сок'
           }    

url_list =['https://www.perekrestok.ru/catalog/makarony-krupy-spetsii/makaronnye-izdeliya?page=',
           'https://www.perekrestok.ru/catalog/konservy-orehi-sousy/ovoschnye-konservy?page=',
           'https://www.perekrestok.ru/catalog/soki-vody-napitki/soki-nektary?page=',   
          ]
product_list =[]

for url in url_list:
    for page in range(1,20):
        url_page = url + str(page)
        product_list += perekrestok_parse(url_page,change)    
for key in product_list:

temp=[]
for i in a:
    if i not in temp:
        temp.append(i)
product_list = temp
print(temp)   