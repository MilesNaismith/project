import csv

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
            check += float(price_list[1][item])
    return price_list[0], round(check, 2)


def main(shopping_list):
    print('запускаем основной скрипт')
    price_list_auchan = get_price('auchan')
    price_list_metro = get_price('metro')
    price_list_perekrestok = get_price('perekrestok')
    check_auchan = get_check(shopping_list,price_list_auchan)
    check_metro = get_check(shopping_list,price_list_metro)
    check_perekrestok = get_check(shopping_list,price_list_perekrestok)
    print('готовим результаты')
    return check_auchan, check_metro, check_perekrestok

if __name__ == "__main__":
    main(shopping_list)
