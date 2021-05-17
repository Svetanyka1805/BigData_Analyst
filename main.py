# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import datetime


class Dat:
    __fDate: datetime
    __dt: str
    __fMonths: list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                     'ноябрь', 'декабрь']
    __name_month: list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                        'Ноябрь', 'Декабрь']

    def __init__(self, pDate):
        try:
            Dat.__fDate = datetime.strptime(pDate, '%d-%m-%Y')
            self.get_datepart()
            print(f"Дата = {Dat.__fDate.day} {Dat.__name_month[Dat.__fDate.month % 12 -1]} {Dat.__fDate.year}")
        except ValueError as ex:
            print(ex.args)
            Dat.__dt = pDate
            print(f"Ошибка в дате {pDate}!\n{self.valid_date(Dat.__dt)}")

    @classmethod
    def get_datepart(cls):
        print({"день": cls.__fDate.day, "месяц": cls.__fDate.month, "год": cls.__fDate.year})

    @staticmethod
    def valid_date(dt: datetime):
        Dat.dt = dt
        ls = [int(i) for i in dt.split("-")]
        if (not (ls[0] in range(1, 32)) and (ls[1] in [1, 3, 5, 7, 8, 10, 12])) or (
                not (ls[0] in range(1, 31)) and (ls[1] in [4, 6, 9, 11])):
            return f"Число дня {ls[0]} не существует в месяце {Dat.__fMonths[ls[1] % 12 - 1]}"

        elif not (ls[1] in range(1, 13)):
            return f"Номер месяца = {ls[1]} не существует. В году всего 12 месяцев"

        elif ls[0] == 29 and ls[1] == 2 and (ls[2] % 4 != 0):
            return f"В году {ls[2]} число {ls[0]} в месяце {Dat.__fMonths[ls[1] % 12 - 1]} не существует"


myDate = Dat(input("Введите дату в формате dd-mm-yyyy: "))
# myDate.get_datepart()


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ErrorDevinionByZero:

    def __init__(self, dividend, divider):

        try:
            print(f"Результат деления = {dividend / divider}")
        except ZeroDivisionError:
            print(f"Ошибка при делении = {dividend} / {divider}. \nДелитель не может бть равен нулю!")

dividend = int(input("Введите делимое = "))
divider = int(input("Введитель делитель = "))
er = ErrorDevinionByZero(dividend, divider)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
from datetime import datetime


class Sklad:

    def __init__(self):
        self.orgtech = dict()
        self.company = dict()

    def add2sklad(self, what, how_much):
        if what in self.orgtech:
            self.orgtech[what] += how_much
        else:
            self.orgtech[what] = how_much

    def delFromsklad(self, what, how_much, whom):
        self.orgtech[what] -= how_much
        self.company[whom] = [what, self.orgtech[what],  datetime.strftime(datetime.today(), '%d-%m-%Y')]

    def get_list_orgtech(self):
        return self.orgtech

    def get_count_tech(self, orgtch):
        return self.orgtech[orgtch]

    def product_movement(self):
        print(self.company)

    def __str__(self):
       return f"Техника на складе:\n{self.orgtech}"


class OrgTech:

    def __init__(self, orgtech):
        if not (orgtech in list_tech):
            list_tech.append(orgtech)

    def __str__(self):
        return f"{self.__class__.__name__}"

    @staticmethod
    def valid_count(count):
        try:
            int(count)
            if int(count) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def show_orgtech():
        print(f"сведения об имеющейся технике: {str(list_tech)}")


class Printer(OrgTech):
    def __init__(self, org_count: int = 0):
        self.orgtech = "принтер"
        self.org_count = org_count


class Scanner(OrgTech):
    def __init__(self, org_count: int = 0):
        self.orgtech = "сканер"
        self.org_count = org_count


class Xerox(OrgTech):
    def __init__(self, org_count: int = 0):
        self.orgtech = "ксерокс"
        self.org_count = org_count

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

sklad = Sklad()
printer = Printer()
scanner = Scanner()
xerox = Xerox()
list_tech = ["принтер", "сканер", "ксерокс"]

tech = input("Введите название техники: ").lower().replace(" ", "")
while tech != "":
    if (tech in list_tech):

        inpt_count = input(f"Введите количество {tech} для заказа ")
        while not OrgTech.valid_count(inpt_count):
            inpt_count = input(f"Количество {inpt_count} введено не корректно! Введите корректное количество {tech} для заказа ")
        count = int(inpt_count)

        if list_tech.index(tech) == 0:
            printer.org_count += count
            res_count = printer.org_count
        elif list_tech.index(tech) == 1:
            scanner.org_count += count
            res_count = scanner.org_count
        elif list_tech.index(tech) == 2:
            xerox.org_count += count
            res_count = xerox.org_count

        print(f"Заказ на {tech} в количестве {count}. Всего количество = {res_count}")

    else:
        print(f"Мы такое не продаем. Вот список нашей продукции: {list_tech}")

    tech = input("Введите название техники или нажмите Enter для окончания ввода: ").lower().replace(" ", "")

print()
print()
print()
# print("созданы объекты: ", printer, scanner, xerox)
OrgTech.show_orgtech()
print()
sklad.add2sklad(printer.orgtech, printer.org_count)
sklad.add2sklad(scanner.orgtech, scanner.org_count)
sklad.add2sklad(xerox.orgtech, xerox.org_count)
# print(sklad.get_list_orgtech())


def get_input_count(inpt_count):
    while not OrgTech.valid_count(inpt_count):
        inpt_count = input(f"Не корректно введено Количество {inpt_count}! Введите корректное количество {tech} для отгрузки ")
    return int(inpt_count)


if input("Хотите распределить технику? да/нет   ").lower() == "да":
    tech = input(f"Какую технику хотите отгрузить? на складе имеются: {sklad.get_list_orgtech()} ").lower().replace(" ", "")
    while tech != "":
        if tech in list_tech:
            inpt_count = input(f"Количество {tech} для отгрузки? (количество на складе {sklad.get_count_tech(tech)}) ")
            count = get_input_count(inpt_count)
            if count > sklad.get_count_tech(tech):
                inpt_count = input(f"К сожалению указанного количесвта {tech} на складе нет. Введите меньшее "
                                  f"количество или '0' для отказа (количество на складе {sklad.get_count_tech(tech)}) ")
                count = get_input_count(inpt_count)

            if not (count == 0):
                company = input("Кому? (имя компании или получателя): ")
                sklad.delFromsklad(tech, count, company)
            tech = input(
                f"Какую технику хотите отгрузить? на складе имеются: {sklad.get_list_orgtech()} ").lower().replace(" ", "")
        else:
            tech = input(f"На складе нет товара {tech}. На складе имеются: {sklad.get_list_orgtech()}"
                         f" Введите из преложенного: ").lower().replace(" ", "")

print()
print()

sklad.product_movement()
print(f"Осталось на складе: {sklad.get_list_orgtech()}")
print()
print("Добавим еще 3 принтера")
sklad.add2sklad(printer.orgtech, 3)
print(f"Осталось на складе: {sklad.get_list_orgtech()}")


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, chislo):
        self.compl_digit = chislo

    def __add__(self, other):

        return self.compl_digit + other.compl_digit

    def __mul__(self, other):
        return self.compl_digit * other.compl_digit

    def __str__(self):
        return str(self.compl_digit)


cdigit1 = ComplexNumber(complex(1, 6))
cdigit2 = ComplexNumber(1 + 0.051j)

print(cdigit1)
print(cdigit2)
print(cdigit1 + cdigit2)
print(cdigit1 * cdigit2)
