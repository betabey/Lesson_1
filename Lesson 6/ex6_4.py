class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The {self.color} {self.name} went!'

    def stop(self):
        return f'The {self.color} {self.name} stopped!'

    def turn_right(self):
        return f'The {self.color} {self.name} turn right'

    def turn_left(self):
        return f'The {self.color} {self.name} turn left'

    def turn_around(self):
        return f'The {self.color} {self.name} turn around'

    def show_speed(self):
        return f'The {self.color} {self.name} is moving at a speed of {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            print(f'Over speed!!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 40:
            print(f'Over speed!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


Mersedes = TownCar(50, 'White', 'Mersedes', False)
Audi = SportCar(100, 'Black', 'Audi', False)
Ford = WorkCar(60, 'Green', 'Ford', False)
BMW = PoliceCar(80, 'Blue', 'BMW', True)

print(Mersedes.color)
print(Mersedes.is_police)
print(Audi.speed)
print(Audi.is_police)
print(Ford.name)
print(Ford.color)
print(BMW.color)
print(BMW.speed)
print(Mersedes.go())
print(Mersedes.turn_left())
print(Audi.turn_around())
print(Audi.show_speed())
print(Ford.stop())
print(Ford.turn_right())
print(BMW.go())
print(BMW.show_speed())