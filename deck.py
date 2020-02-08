"""
A file which holds Deck class declaration
"""
import random
import card

class Deck():
    """
    Class which implements a standard 52 deck with 4 suits
    """
    suits = ["♥", "♢", "♧", "♤",]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for suts in Deck.suits:
            for raks in Deck.ranks:
                self.cards.append(card.Card(raks, suts))

    def __str__(self):
        res = ""
        for crd in self.cards:
            res += crd.rank +crd.suit + " "
        return res

    def pull_card(self):
        """
        Removes a card-object from list of cards of the deck. Returns the removed object
        """
        crd = random.choice(self.cards)
        self.cards.remove(crd)
        return crd

    def reshuffle(self):
        """
        Gets back the deck
        """
        self.cards.clear()
        self.__init__()
