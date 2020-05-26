"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 5.
Задание 2.
Автор: Михаил Духонин
Создан: 26 Май 2020.
Задание:
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в 
каждой строке.

"""

# Функции.

def string_word_count():
    """Открывает файл, созданный в предыдущем задании и возвращает кортеж из двух элементов. Первый - количество строк. Второй - 
    словарь, где ключ - номер строки, а значение - количество слов  в ней."""
    with open('l1.txt', 'r', encoding='utf-8') as f:
        count_strings = f.readlines()
        string_count = len(count_strings)
        word_count = dict()
        for string in enumerate(count_strings):
            word_count[string[0] + 1] = len(string[1].split(' '))
    return (string_count, word_count)
            

def main():
    """Логика программы."""
    t = string_word_count()
    print(t)

# На красоты уже нет времени... :-(

if __name__ == '__main__':
    main()
