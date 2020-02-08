"""
this is a class for a card
"""
class Card():
    """
    this is a class for a card
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"
