words = input('Введтите несколько слов разделенных пробелами')
string = words.split()
b = 10
for i in range(1,len(string)+1):
    if len(string[i-1])>10:

        print(i,'- '+(string[i-1])[:10])
    else:
        print(i,'- '+string[i-1])



