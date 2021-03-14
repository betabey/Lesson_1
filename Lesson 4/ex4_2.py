line = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_line = [line[el] for el in range(1, len(line)) if line[el] > line[el - 1]]
print(new_line)
