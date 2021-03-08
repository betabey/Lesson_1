mounth = int(input('Введите месяц в виде целого число(от 1 до 12) :'))
line = ['Зиме', 'Весне', 'Лету', 'Осени']
if mounth <=2 or mounth == 12 :
    print('Этот месяц относится к ',line[0])
elif mounth >2 and mounth<6:
    print('Этот месяц относится к ',line[1])
elif mounth >=6 and mounth <=8:
    print('Этот месяц относится к ',line[2])
elif mounth >8 and mounth < 12:
    print('Этот месяц относится к ',line[3])
else:
    print('Вы ввели цифру не из диапазона!!!')




