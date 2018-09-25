from bs4 import BeautifulSoup
from selenium import webdriver

def auschan_parse(url,substitution=dict()):
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
change = {'Спагетти-вермишель Makfa, 500г ': 'Спагетти Макфа',
          'Макаронные изделия Makfa, «Перья Любительские», 450г': 'Макароны Макфа',
          'Оливки Maestro de Oliva, без косточек, 300г':'Оливки зеленые',
          'Оливки GONZALEZ чёрные без косточек 425г' : 'Оливки черные',
          'Зеленый горошек «6 соток», свежий, мозгового сорта, 400г': 'Горошек',
          'Кукуруза «6 соток», сахарная, в зернах, 400г':'Кукуруза',
          'Сок «Добрый» яблочный, 2 л.': 'Яблочный сок',
          'Сок гранатовый Nar, 1 л':'Гранатовый сок'
           }    

url_list =['https://www.auchan.ru/pokupki/eda/bakaleja/makarony.html',
           'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/olivki.html',
           'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/goroshek-konservirovanny.html',
           'https://www.auchan.ru/pokupki/eda/voda-i-napitki/soki-nektary.html'             
          ]
product_list =[]
for url in url_list:
    product_list += auschan_parse(url,change)         
print(product_list)    