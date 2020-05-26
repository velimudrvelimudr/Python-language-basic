"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 5.
Задание 3.
Автор: Михаил Духонин
Создан: 26 Май 2020.
Задание:
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины 
дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""

# Импорт
from functools import reduce

# Функции.

def rf():
    """Возвращает список кортежей (фамилия, оклад)."""
    with open('l3.txt', 'r', encoding='utf-8') as f:
        l = [(s.split('\t')[0], s.split('\t')[1].rstrip()) for s in f.readlines()]
        # Второй раз пытаюсь использовать метод  readline, и опять он работает криво...
    return l

def main():
    """Логика программы."""
    sotrudniki = rf()
    bednye = [sot for sot, oklad in sotrudniki if float(oklad) < 20000]
    print(f"Самые бедные сотрудники: {bednye}")
    total = sum([float(oklad) for sot, oklad in sotrudniki])
    print(f'Средний оклад: {(total / len(sotrudniki)):.2f} rub.')


if __name__ == '__main__':
    main()
