
product = []
i = 1
aname = [] #Список наименований товаров
apriсe = []#Список цен на товаров
anum = []#Список количества товаров
aunit = []#Список ед.измерений товаров
while True:
    choice = input('Если нужно внести информацию о новом товаре, нажмите "Т"\n'
                'Если необходимо проанализировать существующий товар, нажмите "А"\n'
                   'Если хотите выйти из сеанса, нажмите "В" ').upper()
    if choice == "Т":
        name = input('Введите название товара : ')
        priсe = int(input('Введите цену товара : '))
        num = int(input('Введите количество товара : '))
        unit = input('Единица измерения : ')
        line = (i, {'Название':name,'Цена':priсe,'Количество':num,'Единица измерения':unit})
        product.append(line)
        i+=1
        aname.append(name)
        apriсe.append(priсe)
        anum.append(num)
        aunit.append(unit)
        print( f'Номер и информация о товаре {product}')
        continue
    if choice == "А":
        analitik = {'Название':aname,'Цена':apriсe,'Количество':anum,'Единица измерения':aunit}
        print(analitik)
    else:
        break
print("Удачи")