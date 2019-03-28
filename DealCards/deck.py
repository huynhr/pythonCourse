from card import Card
from random import shuffle
class Deck:

    def __init__(self):
        suits = Card.valid_suits
        values = Card.valid_values
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def _deal(self, removeNum):
        current_deck_count = self.count()
        if current_deck_count == 0:
            raise ValueError('All cards have been dealt')
        elif current_deck_count < removeNum:
            self.cards = self.cards[current_deck_count:]
        else:
            self.cards = self.cards[removeNum:]

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self.cards


playing_cards = Deck()
print(playing_cards.cards)
print('------------------------------------------AFTER SHUFFLE---------------------------------------------------')
print(playing_cards.shuffle())