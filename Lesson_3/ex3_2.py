#name = input('')
#surname = input('')
#year = input('')
#town = input('')
#email = input('')
#cel_number = input('')
def information (name, surname, year, town, email, cel_number):
    return ' '.join([name, surname, year, town, email, cel_number])
print(information(input('Введите имя : '), input('Введите фамилию : '), input('Введите год рождения : '),
                  input('Город проживания : '), input('Электронная почта : '), input('Номер телефона : ')))