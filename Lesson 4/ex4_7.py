from itertools import count
from math import factorial


def my_fact():
    for el in count(1):
        yield factorial(el)


factor = my_fact()
n = 0
for el in factor:
    if n > 20:
        break
    else:
        print(el)
        n += 1
