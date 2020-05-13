"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 2.
Задание 5.
Автор: Михаил Духонин
Создан: 13 мая  2020
Задание:
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента -
номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {название: компьютер, цена: 20000, количество: 5, eд: шт.}),
(2, {название: принтер, цена: 6000, количество: 2, eд: шт.}), 
(3, {название: сканер, цена: 2000, количество: 7, eд: шт.})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ  характеристика товара, например название, а значение  список значений-характеристик, например список названий товаров.
Пример:
{
название: [компьютер, принтер, сканер],
цена: [20000, 6000, 2000],
количество: [5, 2, 7],
ед: [шт.]
}
"""

tovary = list()
nb = 0

while True:
    tov_name = input("Введите название товара или 'q' для завершения: ")
    if tov_name=='q':
        break
    try:
        tov_tsena = float(input("Введите цену единицы товара: "))
    except ValueError:
        print("вы ввели некорректное значение. Выходим!")
        exit()
    if tov_tsena <= 0:
        print("Цена может быть только положительным числом больше нуля. Выходим!")
        exit()
    try:
        tov_kol = float(input("Введите количество товара: "))
    except ValueError:
        print("Вы ввели некорректное значение. Выходим!")
        exit()
    if tov_kol < 1:
        print("Количество может выражаться только натуральным числом. Выходим!")
        exit()
    tov_ed = input("Введите единицу измерения: ")
    nb += 1
    tovary.append(tuple((nb, {
                              'Название': tov_name,
                              'Цена': tov_tsena,
                              'Количество': tov_kol,
                              'Единица измерения': tov_ed
                             })))

tov_an = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}

for n, t in tovary:
    tov_an['Название'].append(t['Название'])
    tov_an['Цена'].append(t['Цена'])
    tov_an['Количество'].append(t['Количество'])

itog = sum([t * c for t, c in zip(tov_an['Цена'], tov_an['Количество'])])

print("Исходный массив:\n", tovary)
print("Преобразованный массив:\n", tov_an)
print("Покупка на сумму: ", itog, "руб.")
