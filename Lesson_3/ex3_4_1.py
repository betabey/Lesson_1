def my_func(x, y):
    if y > 0:
        print('Вы ввели положительную степень.Введите отрицательную')
        return
    else:
        value1 = abs(y)-1
        value2 = 1/x
        for i in range(value1):
            value2 = value2*value2
        return value2
print(my_func(int(input("Введите действительное положительное число: ")),
              int(input("Введите целое отрицательное число, в которое нужно возвести первое значение: "))))

