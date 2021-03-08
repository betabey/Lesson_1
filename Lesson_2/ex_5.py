line = [7, 5, 4, 4, 3, 2,2]
print(f'Текущий рейтинг - {line}')
n= int(input('Введите число для рейтинга '))
while n !=200:
    for el in range(int(len(line))):
        if line[el]==n:
            line.insert(el+1, n)
            break

        elif line[el]<n and line[el+1]>n:
            line.insert(el+1, n)
        elif line[0]<n :
            line.insert(0, n)
        elif line[-1]>n:
            line.append(n)

    print(line)
    n = int(input('Введите число для рейтинга '))