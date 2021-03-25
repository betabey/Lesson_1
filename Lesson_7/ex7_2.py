class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return round(self.width / 6.5 + 0.5, 2)

    def get_square_j(self):
        return round(self.height * 2 + 0.3, 2)

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c:.2f}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j:.2f}'


coat = Coat(6, 6)
jacket = Jacket(5, 8)
print(coat)
print(jacket)
print(coat.get_square_c())
print(jacket.get_sq_full)
print(jacket.get_square_j())
