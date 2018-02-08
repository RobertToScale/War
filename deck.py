from random import shuffle

suits = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        """Initializes a deck, then builds the deck"""
        # empty list to store deck
        self.deck = []
        # creates the deck from the ranks and suits
        self.build_deck()
        # shuffles deck
        self.shuffle_deck()
        # divides the decks between the players
        self.divide_deck()

    def build_deck(self):
        # for each suit, loops through the ranks and concatenates
        for suit in suits:
            for rank in ranks:
                self.deck.append(suit + rank)

    def shuffle_deck(self):
        # shuffles the deck
        shuffle(self.deck)

    def divide_deck(self):
        # splits the deck in two, one for the player, one for the AI
        self.player_deck = self.deck[:26]
        self.bot_deck = self.deck[26:]