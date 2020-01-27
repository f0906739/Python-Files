# For ___ flips, we'll find which side was flipped more than the other side, and by how much.
from random import randint


class Coin():
    number_flips = 0
    num_heads = 0
    num_tails = 0
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
        # num_heads = 0, num_tails = 1
        for i in cls.flip_results:
            if i == 0:
                cls.num_heads += 1
            elif i == 1:
                cls.num_tails += 1

    # Returns string statement saying who won
    def determine(self):
        if self.num_heads > self.num_tails:
            return f"Heads won by {self.num_heads-self.num_tails} flips."
        elif self.num_tails > self.num_heads:
            return f"Tails won by {self.num_tails-self.num_heads} flips."
        else:
            return "Tie."

    @staticmethod
    def play():
        Coin().setFlips()
        Coin().newResults()
        Coin().setSides()

        print(
            f"\nNumber of Flips: {Coin().number_flips}\nHeads: {Coin().num_heads}\nTails: {Coin().num_tails}\n{Coin().determine()}"
        )


Coin().play()
