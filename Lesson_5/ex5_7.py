dict_one = {}
with open('ex5_7.txt', 'r') as file:
    num = 0
    for lines in file:
        line = lines.split()
        profit = int(line[2]) - int(line[3])
        dict_one[line[0]] = profit
        if profit > 0:
            num += profit

    dict_two = {'average_profit': num / len(line)}
    total_dict = dict_one, dict_two
with open('ex5_7_1.json', 'w') as file:
    file.write(str(total_dict))
