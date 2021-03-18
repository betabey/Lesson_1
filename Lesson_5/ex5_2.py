with open('5second.txt') as file:
    num = 0
    letters = 0
    for el in file:
        num += 1
        letters = len(el) - 1
        print(f'В {num} строке {letters} букв ')
    print(f'Число строк равно : {num}')
