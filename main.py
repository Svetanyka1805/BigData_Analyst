# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# ВАРИАНТ 1
my_file = open("lesson5.txt", 'w')
data = input("Введите что-нибудь, только не пробел: ").strip(" ")
while len(data) > 0:
    my_file.writelines(f"{data}\n")
    data = input("Введите еще что-нибудь или нажмите Enter для заврешения: ").strip(" ")
my_file.close()

# ВАРИАНТ 2
my_file = open("lesson5.txt", 'w')
data = input("Введите что-нибудь, только не пробел: ").strip(" ")
list_data = []
while len(data) > 0:
    list_data.append(f"{data}\n")
    data = input("Введите еще что-нибудь или нажмите Enter для заврешения: ").strip(" ")

my_file.writelines(list_data)
my_file.close()



# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("lesson5.txt") as f_obj:
    data = f_obj.read()
f_obj.close()

data1 = data.split("\n")
data2 = data.replace("\n", " ").split()

print(f"Количество строк в файле = {len(data1)}")
print(f"Количество НЕ пустых строк = {len([i for i in data1 if len(i)>0])}")
print(f"Количество слов = {len([i for i in data2 if len(i)>0])}")



# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce

ls_info = []
f_lesson = open("lesson5_3.txt", 'w')
data = input("Введите фамилию сотрудника и его оклад, через пробел: ")
while len(dt) > 0:
    ls_info.append(f"{' '.join(dt.split())}\n")
    dt = input("Введите фамилию сотрудника и его оклад, через пробел: ")
f_lesson.writelines(ls_info)
f_lesson.close()

f_lesson = open("lesson5_3.txt")
data = f_lesson.read()
f_lesson.close()
ls_info.clear()

ls_info = [el.split() for el in data.split("\n") if len(el) > 0]
ls_res = [el[0] for el in ls_info if int(el[1]) < 20]
my_list = [int(el[1]) for el in ls_info]

avg = reduce(lambda summa, x: summa + x, my_list)/len(my_list)

print(f"Следующие сотрудники имеют оклад менее 20:{chr(10)}{chr(10).join(ls_res)}")
print(f"Средний доход сотрудников = {avg}")



# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
dict_dig = {"one": "один", "two": "Два", "three": "Три", "four": "Четыре"}
line_new: str
file_new = open("lesson5_4_new.txt", 'w')
file_old = open("lesson5_4.txt")
for line in file_old:
    key = line.split()[0]
    line_new = line.replace(key, dict_dig.get(key.lower()).title())
    file_new.writelines(line_new)

file_old.close()
file_new.close()



# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import re, functools

file = open("lesson5_5.txt", 'w')
dt = re.sub('[^0-9 ]', '', input("введите числа через пробел: "))
dt = " ".join(dt.split())
file.write(dt)
file.close()

_sum = functools.reduce(lambda summa, x: summa + x, [int(el) for el in dt.split()])
print(_sum)


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import functools
import re

fl = open("lesson5_6.txt")
data = fl.read()
fl.close()

lst = [elem.split(":") for elem in data.split("\n")]
my_dict = dict()

for el in lst:
    ls = [re.sub('[^0-9 ]', '', elem) for elem in el[1].split()]
    ls = [int(el) for el in ls if el != ""]
    my_dict[el[0]] = functools.reduce(lambda summa, x: summa + x, ls)

print(my_dict)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Подсказка: использовать менеджеры контекста.
from functools import reduce
import json

fl = open("lesson5_7.txt")
ls = []
firms_pr = {}
firms_ub = {}
for line in fl:
    data = [el for el in line.replace("\n", "").split(",")]
    prib = float(data[2].replace(" ", "")) - float(data[3].replace(" ", ""))
    if prib > 0:
        firms_pr[data[0]] = prib
    else:
        firms_ub[data[0]] = prib

    ls.append([data[0], prib])
fl.close()

for_avg = [el[1] for el in ls if el[1] > 0]
avg_profit = reduce(lambda summa, x: summa + x, for_avg)/len(for_avg)
d_avg = dict()
d_avg["Средняя прибыль"] = avg_profit

ls.clear()
ls.append(firms_pr)
ls.append(d_avg)

with open("lesson5.json", 'w') as json_file:
    json.dump(ls, json_file)

print(ls)
print(firms_ub)