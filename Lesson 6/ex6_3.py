class Worker():
    def __init__(self,name, surname, position, wage, bonus ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self,name, surname, position, wage, bonus ):
        super().__init__(name, surname, position, wage, bonus )

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

ful_name = Position('Beidulla', 'Agarzaev', 'ingeneer', 25000, 6000)

print(f'{ful_name.get_full_name()} is an {ful_name.position} with {ful_name.get_total_income()}rub gross')