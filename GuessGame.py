from random import randint


class Guess():
    high = "BRUH THAT'S TOO HIGH YOU DUMB IDIOT!!!"
    low = "OMG THAT'S WAY TOO LOWW!! AGH."
    win = "Congrats. Took you long enough."

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.compMin = min
        self.compMax = max
        # (11/23/19) fixed: !!! INFINITE LOOP IF TARGET IS MAX !!!
        self.target = randint(min, max)
        self.guess = -1
        self.scores = []
        self.highscore = 0

    def setGuess(self):
        self.guess = int(
            input(f"\nEnter number between {self.min} and {self.max}:\n"))

    def message(self):
        if self.guess > self.target:
            return self.high
        elif self.guess < self.target:
            return self.low
        else:
            return self.win

    def selfPlay(self):
        self.setGuess()
        print(self.message())
        while self.guess != self.target:
            self.setGuess()
            print(self.message())
        print(f"Target: {self.target}")

    def replay(self):
        confirm = str(input(
            "Do you want to continue playing until you get a new highscore? Enter 'y' for yes, 'n' for no: "))
        if confirm == 'y':
            return "continue"
        elif confirm == 'n':
            print("\n\nHave a nice day!")
            return "stop"
        else:
            print("Error: wrong input data. Please retry.")
            return self.replay()

    def updateScores(self, average):
        self.scores.append(average)

    def roundReset(self):
        self.compMin = self.min
        self.compMax = self.max
        self.guess = -1
        self.target = randint(self.min, self.max)

    def computerPlayRounds(self, rounds):
        completed_rounds = 0
        guesses = []
        while completed_rounds != rounds:
            while self.guess != self.target:
                # if statement fixes infinite loop bug if target == max
                if self.compMin == self.max-1:
                    self.guess = self.compMax
                else:
                    self.guess = int(
                        (self.compMax-self.compMin)/2+self.compMin)
                guesses.append(self.guess)
                print("")
                print(self.guess)
                print(self.message())
                print("")
                # print("")
                if self.message() == self.low:
                    self.compMin = self.guess
                elif self.message() == self.high:
                    self.compMax = self.guess
            if rounds == 1:
                print(
                    f"Target: {self.target}\nNumber of guesses: {len(guesses)}")
                print("----------------------------------------------------------------------------")
            else:
                print(
                    f"""Target: {self.target}\nNumber of guesses: {len(guesses)}\nAverage number of guesses: {len(guesses)/rounds}""")
                print("----------------------------------------------------------------------------")
            self.roundReset()
            completed_rounds += 1
        self.updateScores(len(guesses)/rounds)

    def computerPlayHighscore(self, rounds=1):
        while self.replay() == "continue":
            print(len(self.scores))
            if len(self.scores) >= 1:
                while self.highscore == min(self.scores):
                    self.computerPlayRounds(rounds)
            elif len(self.scores) == 0:
                self.computerPlayRounds(rounds)
            self.highscore = min(self.scores)
            if self.scores[-1] == self.highscore:
                print(f"NEW HIGHSCORE!!! --> {self.highscore}")

    # def __repr__(self):
    #     return f"Target: {self.target}"


Guess(0, 10_000).computerPlayHighscore()
# str(Guess(0, 10_000))
