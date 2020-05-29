"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 6.
Задание 3.
Автор: Михаил Духонин
Создан: 28 Май 2020.
Задание:
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, 
"bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения 
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных 
данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""

# Функции.

class Worker:
    def __init__(self, w_name, w_surname, w_position, wage, bonus):
        self.name = w_name
        self.surname = w_surname
        self.position = w_position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return (self.name, self.surname)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


def main():
    """Логика программы."""
    p = Position("Иван", "Иванов", "менеджер", 50000, 100)
    
    print(p.get_full_name())
    print(p.get_total_income())
    print(p.position)


if __name__ == '__main__':
    main()
