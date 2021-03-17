line = {'Ivanov': '45', 'Gudkov': '36', 'Lapin': '19', 'Gavrilov': '27'}
with open('5third.txt', 'w+') as file_line:
    num = 0
    sum = 0
    for el, mel in line.items():
        sum += int(mel)
        num += 1
        file_line.write(el + ' : ' + mel + ' т.руб\n')
        if int(mel) < 20:
            print(f'Зарплату меньше 20 т.руб имеет {el}')
        mid = sum / num
    print(f'Средний доход сотрудников равен : {mid:.3f} т.руб')
