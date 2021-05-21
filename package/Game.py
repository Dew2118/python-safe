from .Display import display_object
from .Shoe import Shoe
from .Player import Player
from time import sleep


class Game:
    def __init__(self):
        self.shoe = Shoe(4)
        self.shoe.shuffle()
        self.players = []

    def get_deck(self):
        return self.shoe

    def get_display(self):
        return display_object

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
        a_player_hand = a_player.create_hand()
        a_player_hand.draw(self.shoe, 2)
        return a_player, a_player_hand

    def play(self):
        while self.shoe.get_deck_left() > 0:
            # initialize both players
            player1, player1_hand = self.initialize_player('player1')
            _, dealer_hand = self.initialize_player('dealer')
            result = None
            result = dealer_hand.display_one_card()
            if result == 'break':
                break
            player1_hand.display()
            # play both players
            for player in self.players:
                player.play(self.shoe, self)
            # decide result by comparing dealer hand with each player's hand
            for self.number, hand in enumerate(player1.get_all_hands()):
                display_object.display_decide(self.number, f'Result for {hand.get_name()}')
                self.decide(dealer_hand, hand)
            sleep(3)
            display_object.clear()
            self.players = []

    def decide(self, h1, h2):
        display_object.display_decide(self.number, f'{h1.decide(h2)}', 1)