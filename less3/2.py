"""
Университет GeekBrains
Курс: Основы языка Python.
Урок 3.
Задание 2.
Автор: Михаил Духонин
Создан: 18 мая  2020
Задание:
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name, surname, birthday, city, email, phone):
    """Принимает данные о пользователе и возвращает форматированную строку с ними.
    
    Обязательные именованные параметры:
    name - Имя;
    surname - фамилия;
    birthday - Дата рождения в формате 'ДД.ММ.ГГГГГ';
    city - Город проживания;
    email - Электронная почта;
    phone - Телефон.
    
    """
    return f'{name} {surname} родился {birthday} в городе {city}. Номер его телефона: {phone}, E-Mail: {email}.'

def main():
    uname = input("Введите имя: ")
    usurname = input("Введите фамилию: ")
    ubirthday = input('Введите дату рождения с точностью в формате "ДД.ММ.ГГГГ": ')
    try:
        if not (len(ubirthday) == 10 and 1 <= int(ubirthday[0:2]) <= 31 and 1 <= int(ubirthday[3:5]) <= 12 and int(ubirthday[-4:]) and ubirthday[2] == '.' and ubirthday[5] == '.'):
            print("Вы ввели некорректную дату. Выходим!")
            return None
    except ValueError:
        print("Вы ввели некорректную дату. Выходим!")
        return None
    ucity = input("Введите город проживания: ")
    uemail = input("Введите Электронную почту: ")
    if not (uemail.count('@') == 1and ''.join(reversed(uemail)).index('.') >1):
        print("некорректная электронная почта. Выходим!")
        return None
    uphone = input("Введите номер телефона: ")
    return user_data(name=uname, surname=usurname, birthday=ubirthday, city=ucity, email=uemail, phone=uphone)
    
if __name__ == '__main__':
    result = main()
    if result != None:
        print(result)
