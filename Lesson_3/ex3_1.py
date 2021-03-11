
def numbers (number_1,number_2 ):
    if number_2 == 0:
        print('На ноль делить нельзя')

    else:
        return number_1 / number_2
print(numbers(int(input('Введите первое число : ')),int(input('Введите второе число : ')) ))