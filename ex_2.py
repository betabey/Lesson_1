time =int(input('Введите время в секундах :'))
hour = time // 3600
if hour < 1 :
    minut = time//60
    if minut < 1 :
        sec = time
    else:
        sec = time-(minut*60)
else:
    minut = (time-(hour*3600))//60
    sec = (time -(hour*3600))-(minut * 60)
print(f'{hour} ч:{minut} мин: {sec} сек')
