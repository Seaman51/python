def user_info_print(name, surname, born, town, email, phone):
    print(name, surname, born, town, email, phone)


user_info = {'имя': '', 'фамилия': '', 'год рождения': '', 'город проживания': '', 'email': '', 'телефон': ''}
for user_info_key in user_info:
    user_info[user_info_key] = input(f'Введите {user_info_key} ')
user_info_print(name=user_info['имя'], surname=user_info['фамилия'], born=user_info['год рождения'],
                town=user_info['город проживания'], email=user_info['email'], phone=user_info['телефон'])
