"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 3.
Задание 1.
Автор: Михаил Духонин
Создан: 18 мая  2020
Задание:
1. Реализовать функцию, принимающую два числа (позиционные аргументы) 
и выполняющую их деление. Числа запрашивать у пользователя, 
предусмотреть обработку ситуации деления на ноль.
"""


def chastnoye(x, y):
    """Возвращает частное параметров.
    
    Позиционные параметры:
    x, y: любые числа.
    
    """
    try:
        return x / y
    except ZeroDivisionError:
        print("Делить на нуль нельзя!") # Функция возвращает None.
        return None

def main():
    try:
        n1 = float(input("Введите делимое: "))
        n2 = float(input("Введите делитель: "))
    except ValueError:
        print("Вы ввели не число. Выходим!")
        return None
    return chastnoye(n1, n2)


if __name__ == '__main__':
    result = main()
    if result != None:
        print(round(result, 2))
