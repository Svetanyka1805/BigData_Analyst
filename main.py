# 6* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

ind = 1
res = []
spec = ["название", "цена", "количество", "цвет"]

while True:
    question = input("Добавить новый товар да/нет?") 
    if question.upper() == "НЕТ":
        break
    item = {}  # dict

    for spe in spec:
        user_data = input(f"Введите {spe} ")

        item[spe] = int(user_data) if user_data.isdigit() else user_data

        if user_data.isdigit():  # True or False
            item[spe] = int(user_data)
        else:
            item[spe] = user_data

    result.append(tuple([index, item]))
    index += 1

print(result)

res_dict = {}

for item in spec:
    for _, param in result:
        # param = (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
        if res_dict.get(item):
            res_dict[item].append(param.get(item))
        else:
            res_dict[item] = [param.get(item)]

print(res_dict)