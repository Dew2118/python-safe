from .Display import Display
from .Deck import Deck
from .Player import Player


class Game:
    def __init__(self, stdscr):
        self.display_object = Display(stdscr)
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []

    def get_deck(self):
        return self.deck

    def get_display(self):
        return self.display_object

    def create_player(self, player_name):
        a_player = Player(player_name)
        self.players.append(a_player)
        return a_player

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def initialize_player(self, player_name):
        a_player = self.create_player(player_name)
        a_player_hand = a_player.create_hand(self.display_object)
        a_player_hand.draw(self.deck, 2)
        return a_player, a_player_hand

    def play(self):
        # initialize both players
        player1, player1_hand = self.initialize_player('player1')
        dealer, dealer_hand = self.initialize_player('dealer')
        dealer_hand.display_one_card()
        # play both players
        for player in self.players:
            player.play(self.deck, self)
        # decide result by comparing dealer hand with each player's hand
        for self.number, hand in enumerate(player1.get_all_hands()):
            self.display_object.display_decide(self.number, f'Result for {hand.get_name()}')
            self.decide(dealer_hand, hand)

    def decide(self, h1, h2):
        self.display_object.display_decide(self.number, f'{h1.decide(h2)}', 1)