with open('ex5_5.json', 'w+') as file:
    try:
        num = input('Input several numbers : ')
        file.write(num)
        summ = 0
        line = num.split()
        for el in line:
            summ += int(el)
        print(summ)
    except ValueError:
        print('In line have a letter.Please, write only number.')
