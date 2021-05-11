# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# import logging
# import threading
import time
from functools import reduce


class IncorrectOrder(Exception):
    pass


class TrafficLight:
    def __init__(self, color={}):
        if color != {}:
            self.traf_list = color

    traf_list: dict[str, int] = {'красный': 7, 'желтый': 2, 'зеленый': 5}
    right_order = "красныйжелтыйзеленый"

    def running(self):
        order = reduce(lambda concat, x: concat + x, self.traf_list)
        if order != self.right_order:
            raise IncorrectOrder("Не верный порядок следования цветов!")

        for el in self.traf_list:
            print(el)
            time.sleep(self.traf_list[el])


trafl1 = TrafficLight()
trafl1.running()

trafL2 = TrafficLight({'красный': 2, 'желтый': 2, 'зеленый': 2})
trafL2.running()

trafL3 = TrafficLight({'зеленый': 2, 'красный': 2, 'желтый': 2})
trafL3.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_massa(self):
        return (self._length * self._width * 15 * 5) / 1000


myRoad = Road(1000, 12)
print(f"Масса асфальта = {myRoad.calc_massa()} т")


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"доход = {self._income['wage'] + self._income['bonus']}"


pos = Position("Имя", "Фамилия", "директор", 150250, 125000)
print(pos.get_full_name())
print(pos.get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print(f"машина повернула {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Первышение скорости {self.speed}!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Первышение скорости {self.speed}!")


class PoliceCar(Car):
    pass


TCar = TownCar(120, "желтый", "жигули", False)
TCar.go()
TCar.turn("налево")
TCar.stop()
print(TCar.show_speed())

SCar = SportCar(200, "красно-синий", "ламборджини", False)
print(SCar.show_speed())

WCar = WorkCar(100, "белый", "микроаавтобус мерседес", False)
print(WCar.show_speed())

PCar = PoliceCar(120, "синий", "рено сидан", True)
print(PCar.show_speed())


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw
        self.message = "Запуск отрисовки %s"

    def start_draw(self):
        print(self.message)


class Pen(Stationery):
    def start_draw(self):
        self.message = self.message.replace('%s', self.title)
        super(Pen, self).start_draw()

class Pencil(Stationery):
    def start_draw(self):
        self.message = self.message.replace('%s', self.title)
        super(Pencil, self).start_draw()


class Handle(Stationery):
    def start_draw(self):
        self.message = self.message.replace('%s', self.title)
        super(Handle, self).start_draw()


pen = Pen("ручкой", "отрисовка")
pen.start_draw()

pencil = Pencil("карандашом", "отрисовка")
pencil.start_draw()

handle = Handle("маркером", "отрисовка")
handle.start_draw()