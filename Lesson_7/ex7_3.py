class Kletka:
    def __init__(self, quantity):
        self.quantity = int(quantity)


    def __str__(self):
        return f'Количестко клеток {self.quantity * "*"}'

    def __add__(self, other):
        return Kletka(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Разность отрицательная!')


    def __mul__(self, other):
        return Kletka(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Kletka(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

kletka_1 = Kletka(20)
kletka_2 = Kletka(18)
print(kletka_2)
print(kletka_1 + kletka_2)
print(kletka_1 - kletka_2)
print(kletka_1 / kletka_2)
print(kletka_1.make_order(6))
print(kletka_2.make_order(10))
