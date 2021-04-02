class ZerroError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")



div = ZerroError(24, 0)
print(div.divide_by_null(44, 1))
print(div.divide_by_null(44,0))
print(div.divider)
