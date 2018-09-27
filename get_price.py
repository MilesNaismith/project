import csv
def get_auchan():
    price_list =[]
    with open('auchan.csv', 'r', encoding='utf-8') as f:
        fields = ['title','price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            price_list.append(dict(row))
    return price_list[1:]      
price_list_auchan = get_auchan()

print(price_list_auchan)