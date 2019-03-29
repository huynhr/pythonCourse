from deck import Deck

playing_cards = Deck()
print(playing_cards.deal_card())
print(playing_cards.cards)
print(playing_cards)
print('-------------------------------------------------------------------------------------')
print(playing_cards.deal_hand(53))
print(playing_cards.cards)
print(playing_cards)