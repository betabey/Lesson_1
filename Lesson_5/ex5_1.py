line = []
while True:
    new_word = input("Input a word : ")
    if new_word == '':
        print(line)
        break

    else:
        line.append(new_word+"\n")

with open("first.txt", 'x') as text:
    text.writelines(line)
