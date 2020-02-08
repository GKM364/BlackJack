"""
a class for bankroll
"""
class Bankroll():
    """
    a class for bankroll
    """
    def __init__(self, balance=0):
        self.balance = balance

    def income(self, amount):
        """
        adds to bankroll
        """
        self.balance += amount

    def withdrawal(self, amount):
        """
        removes bankroll
        """
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print(f"Insufficient funds! You have only: {self.balance}")
            return False

    def __str__(self):
        return f"{self.balance}"
