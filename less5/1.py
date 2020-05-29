"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 5.
Задание 1.
Автор: Михаил Духонин
Создан: 26 Май 2020.
Задание:
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных 
свидетельствует пустая строка.

"""

def main():
    """Логика программы."""
    with open('l1.txt', 'w', encoding='utf-8') as f:
        while True:
            s = input('Введите строку, или оставьте пустой для завершения: ')
            if s != '':
                f.write(s + '\n')
            else:
                break


if __name__ == '__main__':
    main()
    print('Записано!')