# Итератор, генерирующий целые числа, начиная с указанного
from itertools import count

for el in count(int(input('Введите число с которого нужно начать : '))):
    if el >= 15:
        break
    else:
        print(el, end=' ')
print('\n')
# Итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import cycle

line = ['Hello', 'How are you', 'Fine', 'name', 'year']
step = 0
for el in cycle(line):
    if step > 15:
        break
    else:
        print(el)
        step += 1
