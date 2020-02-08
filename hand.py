"""
A class for player's hand
"""
import card

class Hand():
    """
    A class for player's hand
    """
    def add_card(self, card1):
        """
        This method adds 1 card to a hand
        """
        self.cards.append(card1)
        self.hand_value()

    def hand_value(self):
        """
        This method count the numerical value of the hand with aces situation in mind
        """
        self.value = 0
        acecount = 0
        for crd in self.cards:
            try:
                tmp = int(crd.rank)
            except ValueError:
                if crd.rank in "JKQ":
                    tmp = 10
                else:
                    tmp = 11
                    acecount += 1
            self.value += tmp
        if self.value > 21 and acecount != 0:
            for _ in range(0, acecount):
                self.value -= 10
                if self.value <= 21:
                    break


    def __init__(self, card1, card2):
        self.cards = []
        self.add_card(card1)
        self.add_card(card2)


    def __str__(self):
        res = ""
        for crd in self.cards:
            res += crd.__str__() + " "
        return res

    def show_hand(self):
        res = ""
        for crd in self.cards:
            res += crd.__str__() + " "
        return res