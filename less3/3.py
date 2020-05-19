"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 3.
Задание 3.
Автор: Михаил Духонин
Создан: 19 мая  2020
Задание:
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""

def max_sum(n1, n2, n3):
    l = [n1, n2, n3]
    l.sort(reverse=True)
    return l[0] + l[1]

def main():
    l = input("Введите три любых числа через пробел: ").split(' ')
    if len(l) == 3:
        try:
            return max_sum(float(l[0]), float(l[1]), float(l[2]))
        except ValueError:
            print("Вы ввели чего-то не то!")
            return None
    else:
        print("Вы ввели что-то не то")
        return None

if __name__ == '__main__':
    result = main()
    if result != None:
        print(result)

