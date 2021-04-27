# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 2, "stroka", 2.3, {"8": 8}, [8,9]]

print(my_list)
print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))
print(type(my_list[3]))
print(type(my_list[4]))
print(type(my_list[5]))


# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

str_list = input('Введите значения  элементов списка через пробел: ')
my_list = str_list.split(" ")
i = 0
print(f"было {my_list}")

#if my_list.__len__() % 2 > 0:
while i < (my_list.__len__()-1):
    per = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i+1] = per
    i += 2

print(f"стало {my_list}")


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
mes = int(input("Введите номер месяца: "))

if mes in range(1, 13):
    print(list[mes-1])
    dict = {1: "зима", 2: "зима", 12: "зима", 3: "весна", 4: "весна", 5: "весна", 6:"лето", 7:"лето", 8:"лето", 9: "осень", 10: "осень", 11: "осень"}
    print(dict[mes])
else:
    print(f"Месяца c номером {mes} не существует")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

stroka = input("Введите предложение: ")
ls = stroka.split(" ")
i=1
for elem in ls:
    print(f"{i}. {elem[0:10:1]}")
    i += 1


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

ls = [7, 5, 3, 3, 2]
num = int(input("Введите рейтинг: "))
i = 0
while i <= ls.__len__()-1:
    if ls[i] == num:
        if (i+1 < ls.__len__()-1) and ls[i+1] == num:
            ls.insert(i, num)
        else:
            ls.insert(i, num)
        break
    elif num > ls[i]:
        ls.insert(i, num)
        break
    i += 1

if i > ls.__len__()-1:
    ls.insert(i, num)
    
print(ls)

# 6* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

ind = 1
res = []
spec = ["название", "цена", "количество", "цвет"]

while True:
    question = input("Добавить новый товар да/нет?")  # Нет нет нЕт  НЕт НеТ НЕТ
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
