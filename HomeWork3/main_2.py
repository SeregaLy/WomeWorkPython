# Домашняя работа по третьему семинару
# Задание № 2 Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город
# проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def get_year(str_year):
    while True:
        get_year = input(str_year)
        if get_year.isdigit():
            if 1900 < int(get_year) <= 2022:
                return str(get_year)
            else:
                print("Введена некоректная дата")


def dossier(name, surname, year, city, email, telephone):
    return (f"{name} {surname} {year} {city} {email} {telephone}")


user_surname = input("Введите фамилию ")
user_name = input("Введите имя ")
user_year = get_year(f"Введите дату рождения {user_name} {user_surname} ")
user_city = input(f"Введите город проживания {user_name} {user_surname} "),
user_email = input(f"Введите электронную почту {user_name} {user_surname} "),
user_telephone = input(f"Введите номер телефона {user_name} {user_surname} ")

print(dossier(surname=user_surname,
              name=user_name,
              year=user_year,
              city=user_city,
              email=user_email,
              telephone=user_telephone))
