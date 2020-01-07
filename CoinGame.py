# For ___ flips, we'll find which side was flipped more than the other side, and by how much.
from random import randint


class Coin():
    number_flips = 0
    heads = 0
    tails = 0
    flip_results = []

    @classmethod
    def setFlips(cls):
        cls.number_flips = int(
            input("\nHow many times do you want to flip the coin?\n"))

    @classmethod
    def newResults(cls):
        cls.flip_results = []
        while len(cls.flip_results) != cls.number_flips:
            cls.flip_results.append(randint(0, 1))

    @classmethod
    def setSides(cls):
        # heads = 0, tails = 1
        for i in cls.flip_results:
            if i == 0:
                cls.heads += 1
            elif i == 1:
                cls.tails += 1

    # Returns string statement saying who won
    def determine(self):
        if self.heads > self.tails:
            return f"Heads won by {self.heads-self.tails} flips."
        elif self.tails > self.heads:
            return f"Tails won by {self.tails-self.heads} flips."
        else:
            return f"Tie."

    @staticmethod
    def play():
        Coin().setFlips()
        Coin().newResults()
        Coin().setSides()

        print(
            f"\nNumber of Flips: {Coin().number_flips}\nHeads: {Coin().heads}\nTails: {Coin().tails}\n{Coin().determine()}")


Coin().play()
