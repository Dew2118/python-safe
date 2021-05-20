import random
from .Card import Card


class Deck:
    def __init__(self):
        value = map(str, ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
        suit = ['C', 'H', 'S', 'D']
        a_deck = [Card(v, s) for v in value for s in suit]
        self.cards = []
        for c in a_deck:
            for a in range(4):
                self.cards.append(c)
        # keep list of drawn cards
        self.drawn = []
    
    def get_deck(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)     

    def get_deck_left(self):
        return len(self.cards)

    def draw(self, number_of_cards):
        if len(self.cards) >= number_of_cards:
            draw = [self.cards.pop(0) for c in range(number_of_cards)]
            self.drawn.extend(draw)
            return draw 

    def update_count(self):
        return sum([card.get_count() for card in self.drawn])
        