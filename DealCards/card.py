class Card:

    valid_suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    valid_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, suit, val):

        if suit not in self.valid_suits:
            raise ValueError(f'{suit} is not a valid value')

        if val not in self.valid_values:
            raise ValueError(f'{val} is not a valid value')

        self.suit = suit
        self.value = val

    def __repr__(self):
        return f'{self.value} of {self.suit}'

