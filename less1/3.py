"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 1.
Задание 3.
Михаил Духонин
29 апреля 2020
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

digit = input('Введите число от 1 до 9: ')

""" Проверяем ввод на корректность """
if not digit.isdigit():
    print('Вы ввели не число. Выходим!')
    exit(0)

if int(digit) < 1 or int(digit) > 9:
    print('Вы ввели недопустимое значение. Выходим!')
    exit(0)

result = int(digit) + int(digit*2) + int(digit*3) # Вычисляем нужное число.

print(result)