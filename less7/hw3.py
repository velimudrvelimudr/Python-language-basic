"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 7.
Задание 3.
Автор: Михаил Духонин
Создан: 01 Июнь 2020.
Задание:
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его 
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы 
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление 
(__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное 
(с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих 
двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет 
организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек 
на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: 
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

# Функции.
class Kletka:
    def __init__(self, cell_count):
        self.cell_count = cell_count # Число ячеек в клетке задаётся при создании экземпляра.

    def __add__(self, othery):
        return Kletka(self.cell_count + othery.cell_count)

    def __sub__(self, othery):
        return Kletka(self.cell_count - othery.cell_count) if self.cell_count > othery.cell_count else "Из меньшей клетки нельзя вычесть большую!"

    def __mul__(self, othery):
        return Kletka(self.cell_count * othery.cell_count)

    def __truediv__(self, othery):
        return Kletka(int(self.cell_count / othery.cell_count))

    def make_order(self, cells_row):
        rows_count, ostatok = divmod(self.cell_count, cells_row)
        return (('*' * cells_row + '\n') * rows_count + ('*' * ostatok)).rstrip()

def main():
    """Логика программы."""
    k1 = Kletka(17)
    k2 = Kletka(5)
    k3 = Kletka(15)

    print(f'''
           "make_order" для клетки из 17 ячеек и 5 ячеек в строке:\n{k1.make_order(5)}
           k1 = {k1.cell_count}, k2 = {k2.cell_count}, k3 = {k3.cell_count}:
           k1 + k2 = {(k1 + k2).cell_count};
           k1 * k2 = {(k1 * k2).cell_count};
           k1 - k3 = {(k1 - k3).cell_count if type(k1 - k3) == Kletka else k1 - k3};
           k3 - k1 = {(k3 - k1).cell_count if type(k3 - k1) == Kletka else k3 - k1};
           k1 / k2 = {(k1 / k2).cell_count}''')

if __name__ == '__main__':
    main()