"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 2.
Задание 1.
Автор: Михаил Духонин
Создан: 13 мая  2020
Задание:
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

l = [1, 2.5, 'kva', True]

for i in l:
    print(i, ' имеет тип:', type(i))
    