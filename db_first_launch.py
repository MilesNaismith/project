from db import db_session, Product
import csv
with open('metro.csv','r', encoding='utf-8') as f:
    fields = ['title', 'price']
    reader = csv.DictReader(f, fields, delimiter =';')
    for row in reader:
        prod = Product(name = row['title'], metro_price = row['price'])
        db_session.add(prod)
db_session.commit()