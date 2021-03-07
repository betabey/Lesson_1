line = [34, 'hi', 45.6, 'hello', True, 85, False, 45.5, 'good for you']
j = 0
for i in range(int(len(line) / 2)):
    line[j], line[j + 1] = line[j + 1], line[j]
    j += 2

print(line)