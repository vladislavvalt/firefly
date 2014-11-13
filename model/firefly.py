__author__ = 'vladvalt'


class Firefly:

    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.energy_val = 0

    def energy(self, energy_func):
        self.energy_val = energy_func(self.position)
        return self.energy_val

    def distance(self, another_firefly):
        if isinstance(another_firefly, Firefly):
            return abs(self.position - another_firefly.position)

    def __str__(self):
        return "Firefly id: " + str(self.id) + ", position: " + str(self.position) + ", energy: " + str(self.energy_val)