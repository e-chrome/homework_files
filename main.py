with open('recipes.txt', encoding="utf-8") as f:
    text = f.read()
cook_book = {}

while text != '':
    name_of_recipe = text[:text.find('\n')]
    text = text[text.find('\n') + 1:]
    if name_of_recipe == '':
        continue
    number_of_ingredients = int(text[:text.find('\n')])
    text = text[text.find('\n') + 1:]
    list_of_ingredients = []
    for i in range(number_of_ingredients):
        dict_ingredient = {}
        line = text[:text.find('\n')]
        if text.find('\n') == -1:
            text = ''
        else:
            text = text[text.find('\n') + 1:]
        ingredient = line[:line.find('|')].rstrip()
        line = line[line.find('|') + 1:]
        quantity = int(line[:line.find('|')])
        measure = line[line.find('|') + 1:].strip()
        dict_ingredient['ingredient_name'] = ingredient
        dict_ingredient['quantity'] = quantity
        dict_ingredient['measure'] = measure
        list_of_ingredients += [dict_ingredient]
    cook_book[name_of_recipe] = list_of_ingredients


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    name_of_ingredient = ''
    quantity_of_ingredient = 0
    measure_of_ingredient = ''

    for dish in dishes:
        ingredients = cook_book.get(dish)
        for ingredient_item in ingredients:
            name_of_ingredient = ingredient_item.get('ingredient_name')
            quantity_of_ingredient = ingredient_item.get('quantity')
            measure_of_ingredient = ingredient_item.get('measure')
            if name_of_ingredient in shop_list:
                old_quantity = shop_list[name_of_ingredient]['quantity']
                shop_list[name_of_ingredient]['quantity'] = old_quantity + quantity_of_ingredient * person_count
            else:
                shop_list[name_of_ingredient] = {
                    'measure': measure_of_ingredient,
                    'quantity': quantity_of_ingredient * person_count
                }
    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))



