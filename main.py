# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from functools import reduce
import copy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        rez = reduce(lambda m, x: str(m) + "\n" + str(x), self.matrix)
        return str(rez)

    def __add__(self, other):
        self.new_matrix = copy.deepcopy(self.matrix)
        for i, row in enumerate(self.new_matrix):
            for j, el in enumerate(row):
                self.new_matrix[i][j] += other.matrix[i][j]
        rez = reduce(lambda m, x: str(m) + "\n" + str(x), self.new_matrix)
        return rez


matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
matr1 = [[2, 1, 3], [4, 5, 6], [7, 8, 9], [0, 1, 1], [3, 1, 5]]
cMatr = Matrix(matr)
cMatr1 = Matrix(matr1)
print(f"first matrix =\n{cMatr}")
print()
print(f"second matrix =\n{cMatr1}")
print()
print(f"addition result =\n{cMatr + cMatr1}")


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes:
    def __init__(self, name, clothes_type, size=0, growth=0):
        self.name = name
        self.type = clothes_type
        self.V = int(size)
        self.H = int(growth)
        self._consumption = {"пальто": self.V / 6.5 + 0.5, "костюм": 2 * self.H + 0.3}
        # return

    @property
    def get_consumption(self):
        return round(self._consumption[self.type], 2)

    @abstractmethod
    def total_consumption(self):
        pass


class Palto(Clothes):

    def __init__(self, name, size, count=1):
        super().__init__(name, "пальто", size=size)
        self.count = count

    def __str__(self):
        return f"Расход ткана на пальто {self.name} = {str(self.get_consumption)}"

    def total_consumption(self):
        return round(self.get_consumption * self.count, 2)


class Suit(Clothes):

    def __init__(self, name, size, count=1):
        super().__init__(name, "костюм", growth=size)
        self.count = count

    def __str__(self):
        return f"Расход ткани на костюм {self.name} = {str(self.get_consumption)}"

    def total_consumption(self):
        return round(self.get_consumption * self.count, 2)


palto = Palto("Пьер Карден", 46, 100)
suit = Suit("Костюм женский", 1.7, 90)
print(palto)
print(palto.get_consumption)
print(palto.total_consumption())
print()
print(suit)
print(suit.get_consumption)
print(suit.total_consumption())


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#     Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#     Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#     Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#     Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
from functools import reduce


class Cell:
    def __init__(self, cells_count: int):
        self.cells_count = cells_count

    def __add__(self, other):
        return self.cells_count + other.cells_count

    def __sub__(self, other):
        return self.cells_count - other.cells_count

    def __mul__(self, other):
        return self.cells_count * other.cells_count

    def __truediv__(self, other):
        return round(self.cells_count / other.cells_count, 0)


    def make_order(self, number_in_row):
        num_rows = self.cells_count // number_in_row
        rem_count = self.cells_count - (number_in_row * num_rows)

        row = reduce(lambda c, x: str(c) + str(x), ["*" for i in range(number_in_row)])
        rows = reduce(lambda c, x: str(c) + '\n' + str(x), [row for i in range(num_rows)])
        if rem_count > 0:
            rem_row = reduce(lambda c, x: str(c) + str(x), ["*" for i in range(rem_count)])
        else:
            rem_row = ""
        return f"{rows}\n{rem_row}"


cell1 = Cell(19)
cell2 = Cell(2)

print(cell1.make_order(4))
print(cell2 + cell1)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
