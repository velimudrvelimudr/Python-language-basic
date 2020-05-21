"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 4.
Задание 7.
Автор: Михаил Духонин
Создан: 21 Май 2020.
Задание:
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен 
создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение 
факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""# Я не понял, как совместить то, что fact на каждой итерации должна возвращать n и вычислять факториал. Получилась какая-то 
# # фигня - fact делает то же, что и range, а, собственно, факториал вычисляется в другом месте. Функция, вычисляющая факториал,
# не может быть итератором, ибо возвращает единственное значение... В общем, получилось, что получилось.

# Функции.

def fact(number):
    for el in range(1, number + 1):
        yield el

def main():
    """Логика программы."""
    f = 1
    for i in fact(5):
        f *= i
    return f


if __name__ == '__main__':
    print(main())
