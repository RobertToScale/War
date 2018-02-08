from game_functions import Game_Functions
from player import Player
from deck import Deck

deck = Deck()
player = Player(deck.player_deck)
opponent = Player(deck.bot_deck)
play = Game_Functions(player, opponent)