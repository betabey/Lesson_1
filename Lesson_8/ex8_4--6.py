class Office_equipment:

    def __init__(self, name, price, quantity, list_number, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numl = list_number
        self.my_fullstore = []
        self.my_store = []
        self.my_line = {'Device model': self.name, 'Unit price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'| Device model - {self.name} | Unit price - {self.price} | Quantity - {self.quantity} |'

    def productInfo(self):
        while True:

            try:
                model = input('Input device model : ')
                prod_price = int(input('Input product price : '))
                prod_quant = int(input('Input quantity of product : '))
                new_string = {'Device model': model, 'Unit price': prod_price, 'Quantity': prod_quant}
                self.my_line.update(new_string)
                self.my_store.append(self.my_line)
                print(f'Current string -\n {self.my_store}')
            except:
                print('Maybe you wrote a "str" in "int" ?!?!?!?\nBe careful!\nTRY AGAIN!!!')
                return Office_equipment.productInfo(self)

            quit = input('Please, if you want write another one - input "Enter"\nIf you want quit - input "Q"').upper()

            if quit == 'Q':
                self.my_fullstore.append(self.my_store)
                print(f'Full store {self.my_fullstore}')
                return f'You done!!!'


class Scanner(Office_equipment):
    def to_scan(self):
        return f'Scanner will send in {self.numl} days!'


class Copier(Office_equipment):
    def to_copier(self):
        return f'Copier will send in {self.numl} days!'


class Printer(Office_equipment):
    def to_print(self):
        return f'Printer will send in {self.numl} days!'


unit_1 = Printer('Samsung', 6500, 3, 25)
unit_2 = Copier('HP', 3200, 6, 7)
unit_3 = Scanner('LG', 4600, 4, 8)
print(unit_1)
print(unit_2)
print(unit_3)
print(unit_2.to_copier())
print(unit_1.productInfo())
print(unit_3.productInfo())
