from functools import reduce

line = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список четных чисел : \n{line}')


def my_func(pre_el, el):
    return pre_el * el


print(f'Произведение всех чисел из списка : {reduce(my_func, line)}')
