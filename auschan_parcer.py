from bs4 import BeautifulSoup
import urllib.request
def main():
    parse(get_html('https://www.auchan.ru/pokupki/eda/bakaleja/makarony.html'))
    
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    section = soup.find("div",{"class": "products__list"})
    rows = section.find_all("div",{"class": "products__item-inner"})
    print(rows)
    print(len(rows))
if __name__ =='__main__':
    main()   