
def my_sum():
    total = 0
    el = False
    while el == False:
        line = input('Введите список натуральных чисел через пробел.\nЧтобы '
                     'выйти из системы введите "done" : ').split()
        sumnum = 0
        for i in range(len(line)):

            if line[i] == 'done' or line[i] == 'Done':
                el = True
                break
            else:
                sumnum = sumnum + int(line[i])
        total += sumnum
        print('Сумма  нововведенных чисел равна : ',sumnum)

    return total
print('Общая сумма всех введеных чисел равна : ',my_sum())
