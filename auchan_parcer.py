from bs4 import BeautifulSoup
from selenium import webdriver
import csv

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
def substitution():
    product_list = dict()
    with open('auchan_replace.csv', 'r', encoding='utf-8') as f:
        fields =['name_old', 'name_new']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            product_list[row['name_old']] = row['name_new']
    return product_list     

def main():
    url_list = ['https://www.auchan.ru/pokupki/eda/bakaleja/makarony.html',
                'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/olivki.html',
                'https://www.auchan.ru/pokupki/eda/konservacija/ovoschnye-konservy/goroshek-konservirovanny.html',
                'https://www.auchan.ru/pokupki/eda/voda-i-napitki/soki-nektary.html'             
                   ]
    change = substitution()
    product_list_auchan = []
    for url in url_list:
        product_list_auchan += auchan_parse(url, change)         
    
    with open('auchan.csv','w', encoding='utf-8') as f:
        fields = ['title', 'price']
        writer =csv.DictWriter(f,fields,delimiter =';')
        writer.writeheader()
        for item in product_list_auchan:
            writer.writerow(item)

if __name__ == "__main__":   
    main()    