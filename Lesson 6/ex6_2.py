class Road:
    spec_grav = 0.025  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см в тоннах

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class Mass(Road):
    def __init__(self, _length, _width, thickness):
        super().__init__(_length, _width)
        self.thickness = thickness

    def mass(self):
        return (self._length * self._width * self.thickness * self.spec_grav)


r = Mass(20, 5000, 5)
print(r.mass())
