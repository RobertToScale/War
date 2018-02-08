class Game_Functions:
    def __init__(self, player, opponent):
        """Main portion of the game"""

        # initializes the player and opponent objects into the game
        self.player = player
        self.opponent = opponent

        print("Press enter to begin.")
        input()

        # sets a loop to keep playing until the player wants to stop
        cont = 'y'
        while cont == 'y':

            # an empty list to store winner's cards, refreshed each turn
            self.pot = []
            # pops the first card out of the deck to be compared
            self.p_card1 = self.player.deck.pop(0)
            self.o_card1 = self.opponent.deck.pop(0)
            # adds the cards to the pot of winner's cards
            self.pot.append(self.p_card1)
            self.pot.append(self.o_card1)

            # displays each player's card
            print("Player Card: " + self.p_card1)
            print("Opponent Card: " + self.o_card1)

            # compares player card to opponent card and gives a return value
            winner = self.compare(self.p_card1, self.o_card1)

            # uses return value to calculate who won and give cards
            self.check_winners(winner)

            print()
            # print number of cards each player has
            print("Player deck size: " + str(len(player.deck)))
            print("Opponent deck size: " + str(len(opponent.deck)))

            cont = input("Play again? y/n: ")
            print("\n\n")

        # prints each player's deck on exit
        print("Player Deck: ")
        print(player.deck)
        print("Opponent Deck: ")
        print(opponent.deck)

        print()
        print("Press enter to end.")
        input()

    def check_winners(self, winner):
        # determine winner
        if winner == 0:
            print("Player wins! Gets: " + str(self.pot))
            # if the player wins, give him the pot
            self.player.deck.extend(self.pot)
        if winner == 1:
            print("Opponent wins!" + str(self.pot))
            # if the opponent wins, give him the pot
            self.opponent.deck.extend(self.pot)
        if winner == 2:
            print("WAR!")
            # if neither player wins, add their top 3 cards to the pot before playing again
            self.pot.append(self.player.deck.pop(0))
            self.pot.append(self.player.deck.pop(0))
            self.pot.append(self.player.deck.pop(0))

            self.pot.append(self.opponent.deck.pop(0))
            self.pot.append(self.opponent.deck.pop(0))
            self.pot.append(self.opponent.deck.pop(0))

            # pop next card from each player and play again
            self.p_card1 = self.player.deck.pop(0)
            print("Player Card: " + self.p_card1)
            self.pot.append(self.p_card1)

            self.o_card1 = self.player.deck.pop(0)
            print("Opponent Card: " + self.o_card1)
            self.pot.append(self.o_card1)

            winner = self.compare(self.p_card1, self.o_card1)

            self.check_winners(winner)

    def compare(self, p_card, o_card):
        # sets up card values for Jack, Queen, King, Ace
        self.p_card_value1 = p_card[1]
        if self.p_card_value1 == 'J':
            self.p_card_value1 = 11
        elif self.p_card_value1 == 'Q':
            self.p_card_value1 = 12
        elif self.p_card_value1 == 'K':
            self.p_card_value1 = 13
        elif self.p_card_value1 == 'A':
            self.p_card_value1 = 14
        else:
            self.p_card_value1 = int(self.p_card_value1)

        self.o_card_value1 = self.o_card1[1]
        if self.o_card_value1 == 'J':
            self.o_card_value1 = 11
        elif self.o_card_value1 == 'Q':
            self.o_card_value1 = 12
        elif self.o_card_value1 == 'K':
            self.o_card_value1 = 13
        elif self.o_card_value1 == 'A':
            self.o_card_value1 = 14
        else:
            self.o_card_value1 = int(self.o_card_value1)

        # compares card value
        if self.p_card_value1 > self.o_card_value1:
            return 0
        elif self.o_card_value1 > self.p_card_value1:
            return 1
        elif self.p_card_value1 == self.o_card_value1:
            return 2