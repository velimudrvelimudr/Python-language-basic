"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 7.
Задание 1.
Автор: Михаил Духонин
Создан: 01 Июнь 2020.
Изменён: 02 Июнь 2020
Задание:
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать 
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
	31	22
	37	43
	51	86
	***	
	3	5	32
	2	4	6
	-1	64	-8
***
	3	5	8	3
	8	3	7	1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица. 
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым 
элементом первой строки второй матрицы и т.д.

"""
# import

from copy import deepcopy

# Функции.

class Matrix:
    def __init__(self, ex_matrix):
        self.matrix = deepcopy(ex_matrix)
        """Чтобы в экземпляр  передавалась сама переменная, а не её копия необходимо использовать функцию deepcopy() из модуля 
           copy. ex_matrix.copy() здесь не помогает."""

    def __str__(self):
        total_string = ''
        for rows in self.matrix:
            for m_item in rows:
                total_string += "\t" + str(m_item)
            total_string += '\n'
        return total_string.strip().replace('\n\t', '\n')


    def __add__(self, other):
        new_matrix = Matrix([])
        for row in range(0, len(self.matrix)):
            new_matrix.matrix.append([])
            for cell in range(0, len(self.matrix[0])):
                new_matrix.matrix[row].append(self.matrix[row][cell] + other[row][cell])
        return new_matrix


def main():
    """Логика программы."""
    l1 = [[1, 2, 3], [4, 5, 6]]
    print (l1, "\nИсходный список, который передаётся в экземпляр")
    l2 = [[9, 8, 7], [6, 5, 4]]
    print(l2, "\nСписок, участвующий в сложении")
    mx = Matrix(l1)
    print(mx, "\nвывод исходного экземпляра Matrix (__str__)")
    mxsum = mx + l2
    print(mxsum, "\nРезультат суммирования (__add__)")
    mx.matrix[0][0] = 0
    print("Матрица после изменения:\n", mx, "\nИсходный список после изменения матрицы:\n", l1, 
          "\nПосле операции mx.matrix[0][0] = 0. l1 благодаря использованию функции copy.deepcopy не изменилась.")


if __name__ == '__main__':
    main()