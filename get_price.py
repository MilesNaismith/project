import csv

shopping_list = ['Кукуруза','Горошек','Спагетти Макфа','Яблочный сок','Оливки зеленые','Макароны Макфа','Спагетти Макфа']
def get_price(name):
    price_list =dict()
    file_name = name + '.csv'
    with open(file_name, 'r', encoding='utf-8') as f:
        fields = ['title','price']
        reader = csv.DictReader(f, fields, delimiter =';')
        for row in reader:
            price_list[row['title']] = row['price']
    return name, price_list     

def get_check(shopping_list, price_list):
    check = 0
    for item in shopping_list:
        if item in price_list[1]:
            check +=float(price_list[1][item])
    return price_list[0], round(check, 2)

price_list_auchan = get_price('auchan')
price_list_metro = get_price('metro')
#price_list_perekrestok = get_price('perekrestok')
check_auchan = get_check(shopping_list,price_list_auchan)
check_metro = get_check(shopping_list,price_list_metro)
print(check_auchan)
print(check_metro)