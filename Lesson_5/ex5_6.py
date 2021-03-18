with open('ex5_6.txt', 'w+') as file:
    dict = {}
    word = "Информатика: 100(л) 50(пр) 20(лаб).\nФизика: 30(л) 50(пр) — 10(лаб)\nФизкультура: 20(теор) — 30(пр) —"
    file.write(word)

with open('ex5_6.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        summ = 0
        new_line = line.replace('(', ' ').split()
        for el in new_line:
            if el.isdigit():
                summ += int(el)
        line = line.split()
        dict[line[0]] = summ
    print(dict)
