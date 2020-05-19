"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 3.
Задание 6.
Автор: Михаил Духонин
Создан: 19 мая  2020
Задание:
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв 
и возвращающую его же, но с прописной первой буквой. Например: 
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, 
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
"""

def first_upper(w):
    if w.isascii() and w.isalpha() and w.islower():
        return w.title()
    else:
        print("Это не слово из строчных латинских букв!")
        return None

def all_first_upper(s):
    list_word = list()
    if s.isascii() and s.islower():
        for w in s.split(' '):
            list_word.append(first_upper(w))
        return ' '.join(list_word)
    else:
        print("Это не правильное предложение!")
        return None


def main():
    sentence = input("Введите предложение из строчных латинских букв без знаков препинания (только буквы и пробелы): ")
    return all_first_upper(sentence)

if __name__ =='__main__':
    result = main()
    if result != None:
        print(result)
