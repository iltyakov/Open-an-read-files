from pprint import pprint
import os

BASE_PATH = os.getcwd()
CB_DIR_NAME = 'Cookbook'
CB_FILE_NAME = 'Cookbook.txt'

full_path = os.path.join(BASE_PATH, CB_DIR_NAME, CB_FILE_NAME)
#ДЗ1

with open(full_path, encoding="utf-8") as receipt_file:
    cook_book = {}
    for line in receipt_file:
        dishes = line.strip()
        ingredient_count = int(receipt_file.readline().strip())
        dish = []
        for item in range(ingredient_count):
            ingredient_list = receipt_file.readline().strip().split('|')
            d_number = {}
            for ads in range(len(ingredient_list)):
                d_number['ingredient_name'] = ingredient_list[0]
                d_number['quantity'] = ingredient_list[1]
                d_number['measure'] = ingredient_list[2]
            dish.append(d_number)
        receipt_file.readline()
        cook_book[dishes] = dish

pprint(cook_book, sort_dicts=False)

#ДЗ2
def get_shop_list_by_dishes(Full_path, dishes, person_count):
    result = {}
    menu = list(cook_book.keys())
    for dish in dishes:
        if dish not in menu:
            print(f'Блюда с названием: {dish} - нет в меню.')
        order = cook_book[dish]
        for ingredient in order:
            i_name = ingredient['ingredient_name']
            if ingredient['ingredient_name'] not in result:
                i_quan = int(ingredient['quantity']) * int(person_count)
                i_maen = ingredient['measure']
                result[i_name] = {'measure': i_maen, 'quantity': i_quan}
            else:
                result[i_name]['quantity'] += int(ingredient['quantity']) * int(person_count)
    return result


pprint(get_shop_list_by_dishes(full_path, ['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)

