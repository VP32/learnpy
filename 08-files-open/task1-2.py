def read_receipes(filename):
    cook_book = {}
    with open('recipes.txt', 'rt', encoding='utf-8') as f:
        while True:
            cook = f.readline()
            if cook == '':
                break

            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient = f.readline().strip()
                ingredient_data = ingredient.split(' | ')
                ingredients.append({'ingredient_name': ingredient_data[0], 'quantity': int(ingredient_data[1]),
                                    'measure': ingredient_data[2]})
            f.readline()
            cook_book.setdefault(cook.strip(), ingredients)

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            continue
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list.setdefault(ingredient['ingredient_name'],
                                     {'measure': ingredient['measure'],
                                      'quantity': ingredient['quantity'] * person_count})

    return shop_list


cook_book = read_receipes('recipes.txt')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
