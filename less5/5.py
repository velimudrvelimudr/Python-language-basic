"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 5.
Задание 5.
Автор: Михаил Духонин
Создан: 26 Май 2020.
Задание:
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""

# Импорт
from l2 import gen_rand_list
# Однако, популярная функция оказалась...

def main():
    """Логика программы."""
    h_numbers = gen_rand_list(0, 100, 1, 10)
    with open('l5_in.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, h_numbers)))
    
    with open('l5_in.txt', 'r', encoding='utf-8') as f:
        s = f.read()
    e_numbers = [int(n) for n in s.split(' ')]
    return sum(e_numbers)


if __name__ == '__main__':
    print("Сумма чисел в файле равна " + str(main()))
