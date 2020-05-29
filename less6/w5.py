"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 6.
Задание 5.
Автор: Михаил Духонин
Создан: 28 Май 2020.
Задание:
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В 
каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

# Функции.
class Stationery:
    def __init__(self):
        self.title = "Канцелярская принадлежность"

    def draw(self):
        return "Нечего рисовать!"

class Pen(Stationery):
    def __init__(self):
        self.title = "Ручка"

    def draw(self):
        return "Начата отрисовка ручки."

class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        return "Отрисовка карандаша"

class Handle(Stationery):
    def __init__(self):
        self.title = "Маркёр"

    def draw(self):
        return "Отрисовка маркёра."
def main():
    """Логика программы."""
    st = Stationery()
    ps = Pen()
    pcs = Pencil()
    hs = Handle()
    
    print(f'''
              {st.title}, {st.draw()}\n
              {ps.title}, {ps.draw()}\n
              {pcs.title}, {pcs.draw()}\n
              {hs.title}, {hs.draw()}
           ''')


if __name__ == '__main__':
    main()
