with open('receipe', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dishes = line.strip()
        ingridients_count = int(f.readline())
        ingridients = []
        for i in range(ingridients_count):
            ingridient = f.readline().strip()
            name, count, measure = ingridient.split('|')
            ingridients.append({
                'ingridient_name': name,
                'quantity': count,
                'measure': measure
            })
        f.readline()
        cook_book[dishes] = ingridients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for elem in dishes:
        for v in cook_book[elem]:
            for key, value in v.items():
                name = v['ingridient_name']
                measure = v['measure']
                quantity = int(v['quantity']) * person_count
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity
                }
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
