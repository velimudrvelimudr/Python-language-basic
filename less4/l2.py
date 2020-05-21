"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 4.
Задание 2.
Автор: Михаил Духонин
Создан: 21 Май 2020.
Задание:
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

"""
# Импорт
from random import randrange

# Функции.

def gen_rand_list(start, end, step, count):
    """Генерирует список случайных чисел из count элементов в диапазоне start - end, с шагом step."""
    result = [randrange(start, end, step) for i in range(count)]
    return result

def filt(in_list):
    """Фильтрует список в соответствии с условием задачи."""
    out_list = [in_list[i] for i in range(1, len(in_list), 1) if in_list[i] > in_list[i-1]]
    return out_list

def main():
    """Логика программы."""
    in_list = gen_rand_list(0, 100, 1, 10)
    print(in_list)
    out_list = filt(in_list)
    print(out_list)


if __name__ == '__main__':
    main()
