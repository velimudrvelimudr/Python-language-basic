"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 4.
Задание 1.
Автор: Михаил Духонин
Создан: 21 Май 2020.
Задание:
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо 
использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо 
запускать скрипт с параметрами.

"""

# Импорт
from sys import argv

# Функции.

def zp(hours, stavka, prem):
    """Рассчёт заработной платы"""
    return (hours * stavka) + prem

def main():
    """Логика программы."""
    try:
        hours = float(argv[1])
        stavka = float(argv[2])
        prem = float(argv[3])
    except ValueError:
        print("Некорректные параметры. Ничего не делаем!")
        return None
    return zp(hours, stavka, prem)

if __name__ == '__main__':
    result = main()
    if result != None:
        print(f'Сотрудник заработал {result:.2f} руб.')
