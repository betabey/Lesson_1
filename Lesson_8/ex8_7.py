class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.x = 'a + b * j'

    def __add__(self, other):
        print(f'Сумма x1 и x2 равна')
        return f'x = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print(f'Произведение x1 и x2 равно')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'


x_1 = ComplexNum(4, 3)
x_2 = ComplexNum(-2, 1)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)
