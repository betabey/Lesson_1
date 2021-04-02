class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def numbering(cls, day_month_year):
        new_date = []
        for el in day_month_year.split():
            if el != '-':
                new_date.append(el)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.numbering(self.day_month_year)}'


today = Data('2 - 4 - 5')
print(today)
print(Data.numbering('5 - 11 - 2008'))
print(Data.valid(30, 2, 1033))
print(Data.valid(34, 30, 1033))
