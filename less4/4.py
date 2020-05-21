"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 4.
Задание 4.
Автор: Михаил Духонин
Создан: 21 Май 2020.
Задание:
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих 
требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

"""

# Импорт
from l2 import gen_rand_list
# Пришлось переименовать один из файлов с предыдущим заданием, чтобы его можно было импортировать...

# Функции.

def net_povtor(in_list):
    return [i for i in in_list if in_list.count(i) == 1] # решение задачи

def main():
    """Логика программы."""
    in_list = gen_rand_list(1,10,1, 15)
    out_list = net_povtor(in_list)
    print(in_list)
    print(out_list)


if __name__ == '__main__':
    main()
