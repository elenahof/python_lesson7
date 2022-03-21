class Clothes:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat(self):
        return self.width / 6.5 + 0.5

    def suit(self):
        return self.height * 2 + 0.3

    @property
    def consumption(self):
        return str(f'Total consumption: \n'
                   f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.coatsize = self.width / 6.5 + 0.5

    def __str__(self):
        return f"Coat fabric consumption: {self.coatsize}"


class Suit(Clothes):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.suitsize = self.height * 0.2 + 0.3

    def __str__(self):
        return f"Suit fabric consumption: {self.suitsize}"


coat_s = Coat(3, 5)
suit_s = Suit(2, 6)
print(coat_s)
print(suit_s)
print(coat_s.consumption)
print(suit_s.consumption)