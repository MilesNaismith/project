from db import db_session, Product
import csv
def main():
    with open('metro.csv','r', encoding='utf-8') as f:
        fields = ['title', 'price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            prod = Product.query.filter(Product.name==row['title']).first()
            prod.metro_price = row['price']


    with open('auchan.csv','r', encoding='utf-8') as f:
        fields = ['title', 'price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            prod = Product.query.filter(Product.name==row['title']).first()
            prod.auchan_price = row['price']

    with open('perekrestok.csv','r', encoding='utf-8') as f:    
        fields = ['title', 'price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            prod = Product.query.filter(Product.name==row['title']).first()
            prod.perekrestok_price = row['price']

    db_session.commit()

if __name__ == "__main__":
    main()