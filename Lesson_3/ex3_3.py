def sum (arg1, arg2, arg3):
    if arg1>=arg2 and arg2>=arg3:
        return arg1 + arg2
    elif arg1<=arg2 and arg1<=arg3:
        return arg2 + arg3
    else:
        return  arg1 + arg3
print(sum(int(input('First value : ')), int(input('Second value : ')), int(input('Third value : '))))