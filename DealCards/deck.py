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

        actual = min([removeNum, current_deck_count])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]

        return cards


    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')

        shuffle(self.cards)
        return self.cards

    def deal_card(self): 
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)

playing = Deck()
hand = playing.deal_card()

print(hand)