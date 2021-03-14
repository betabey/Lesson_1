from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Заработная плата сотрудника составляет {res} т.рублей')
    print(f'Из них премия за выполнение плана составляет : {bonus} т.рублей')
except ValueError:
    print('Значение не является числовым')
