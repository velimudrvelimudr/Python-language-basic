"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 1.
Задание 2.
Михаил Духонин
29 апреля 2020
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
t = int(input('Введите количество секунд не превышающее 86400'))

if t < 1 or t > 86400:
    # Не даём пользователю ввести количество секунд большее, чем в сутках.
    print('введённое число находится вне допустимого диапазона. Выходим!')
    exit(0)

h, s = t // (60**2), t % (60**2)
min, sec = s // 60, s % 60

print(f'{h:0=2}:{min:0=2}:{sec:0=2}')
# В выводе в начале чисел, если они меньше 10, добавляются нули, дополняя их до двух цифр.
