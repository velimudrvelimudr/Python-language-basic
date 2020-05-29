"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 6.
Задание 4.
Автор: Михаил Духонин
Создан: 28 Май 2020.
Задание:
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).  А 
также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите 
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен 
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости 
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов 
методов и также покажите результат.

"""

# Функции.
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self._speed = speed
        self.is_police = is_police

    def go(self):
        return "Поехали!"

    def stop(self):
        return "Встали!"

    LEFT = "На лево!"
    RIGHT = "На право!"

    def turn(self, direction):
        if direction == self.RIGHT or direction == self.LEFT:
            return "Поворот " + direction
        else:
            return "Сломали руль!"


    def show_speed(self):
        return self._speed

class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            return "Превышена скорость на " + str(self._speed - 60) + " км/ч"
        else:
            return self._speed

class SportsCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            return "Превышена скорость на " + str(self._speed - 40) + " км/ч"
        else:
            return self._speed

class PoliceCar(Car):
    pass

def main():
    """Логика программы."""
    # Создаём машины:
    c = Car("Автомобиль", "Любой", 0)
    tc = TownCar("Жигули", "Белый", 60)
    wc = WorkCar("Нива", "Серый", 50)
    sc = SportsCar("Феррари", "Красный", 180)
    pc = PoliceCar("УАЗ", "болотный", 0, True)
    
    # Тестируем классы.
    print(f'''
              Машина: {c.name}, цвет: {c.color}, Движется со скоростью: {c.show_speed()} км/ч\n
              {c.go()}, {c.stop()}, {c.turn(Car.LEFT)}, {c.turn(Car.RIGHT)}\n\n
              Машина: {wc.name}, цвета {wc.color}, Движется со скоростью {wc.show_speed()}\n
              {wc.go()}, {wc.stop()}, {wc.turn("На право!")}, {wc.turn("На лево!")}. Находится в полиции: {"ДА" if wc.is_police else "нет"}.\m\m
              Машина: {tc.name}, цвета {tc.color}, Движется со скоростью: {tc.show_speed()}\n
              Машина {sc.name}, цвета {sc.color}, Движется со скоростью {sc.show_speed()} км/ч.\n
              Машина {pc.name}, цвета {pc.color}, Движется на скорости {pc.show_speed()} км/ч. Находится в полиции: {"Да!" if pc.is_police else "Нет!"}
           ''')

if __name__ == '__main__':
    main()
