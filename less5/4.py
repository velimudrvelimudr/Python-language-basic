"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 5.
Задание 4.
Автор: Михаил Духонин
Создан: 26 Май 2020.
Задание:
Создать (не программно) текстовый файл со следующим содержимым: 
One  1
Two  2
Three  3
Four  4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""


def main():
    """Логика программы."""
    with open('l4_in.txt', 'r', encoding='utf-8') as f:
        numbers = [s.split(' ')[1] for s in f.readlines()]
    with open('l4_out.txt', 'w', encoding='utf-8') as f:
        for n in numbers:
            f.write(n)


if __name__ == '__main__':
    main()
    print('Готово!')
