class Stationery :
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки "{self.title}", выполненная ручкой.'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки "{self.title}", выполненная карандашом.'


class Handle (Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки "{self.title}", выполненная маркером.'

pen=Pen('Shine')
pencil = Pencil('The game')
handle = Handle('OBEY')
print(pen.title)
print(pen.draw())
print(pencil.title)
print(pencil.draw())
print(handle.title)
print(handle.draw())
