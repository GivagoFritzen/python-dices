import random


class Dice:
    list_numbers = []
    min = 0
    max = 0

    def __init__(self, min, max):
        self.list_numbers = []
        self.min = min
        self.max = max

    def random(self):
        number = random.randint(self.min, self.max)
        self.list_numbers.append(number)
        return number
