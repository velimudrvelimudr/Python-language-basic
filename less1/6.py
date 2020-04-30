"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 1.
Задание 6.
Михаил Духонин
29 апреля 2020
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число  номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата  не менее 3 км
"""

try:
    a = float(input('Введите начальный результат бегуна в км: '))
    b = float(input('Введите конечный результат, которого должен достичь бегун в км: '))
except ValueError:
    print('Некорректный ввод. Выходим!')
    exit(0)

if a > b:
    print('Конечный результат меньше начального... Выходим!')
    exit(0)

# Задаём начальные значения переменных.
result = a
day = 1

while result < b:
    result += result / 100 * 10
    day += 1
    
print(f'Спортсмен достиг запланированного результата в {int(b)} км на {int(day)}-й день.')

# Наверное есть более красивый способ отбрасывания дробной части, но что-то я уже не вспоминаю...
