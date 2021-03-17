import json

with open('ex5_4.json', 'r') as file:
    line = dict(json.load(file))
translate = ('odin', 'dva', 'tree', 'chetiri')
num = 0
with open('ex5_4_1.json', 'w+') as new_file:
    for el, mel in line.items():
        el = translate[num]
        print(f'{el} - {mel}')
        new_file.write(f'{el} - {mel}\n')
        num += 1
