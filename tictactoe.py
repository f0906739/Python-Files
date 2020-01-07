def log(func):
    def wrapper(*args, **kwargs):
        try:
            print(func.__name__, args, kwargs)
            return func(*args, **kwargs)
        except:
            print("error")
            print(tictactoe().row)
            raise
    return wrapper


class tictactoe():
    # rows.
    first = ["-", "-", "-"]
    second = ["-", "-", "-"]
    third = ["-", "-", "-"]

    # int version of the rows/columns
    row = -1
    column = -1

    player = 1

    @log
    def switchPlayer(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    @log
    def chooseSpot(self):
        self.row = int(
            input(f"Player {self.player}: Pick a row from 1 (top) to 3 (bottom): "))
        self.column = int(
            input(f"Player {self.player}: Pick a column from 1 (left) to 3 (right): "))

    @log
    def getRow(self):
        if self.row == 1:
            return self.first
        elif self.row == 2:
            return self.second
        elif self.row == 3:
            return self.third

    @log
    def draw(self):
        # how to change getRow into getSpot???
        if self.getRow()[self.column-1] != "-":
            # decide spot again
            self.reDraw()
        if self.player == 1:
            self.getRow()[self.column-1] = "O"
        elif self.player == 2:
            self.getRow()[self.column-1] = "X"

    # checks if anyone won and returns player as int
    @log
    def checkWin(self):
        # tie game is checked in first if statement
        if "-" in self.first+self.second+self.third:
            # Horizontal
            if self.first[0] == self.first[1] and self.first[0] == self.first[2]:
                return self.convertLetter(self.first[0])
            elif self.second[0] == self.second[1] and self.second[0] == self.second[2]:
                return self.convertLetter(self.second[0])
            elif self.third[0] == self.third[1] and self.third[0] == self.third[2]:
                return self.convertLetter(self.third[0])
            # Vertical
            elif self.first[0] == self.second[0] and self.first[0] == self.third[0]:
                return self.convertLetter(self.first[0])
            elif self.first[1] == self.second[1] and self.first[1] == self.third[1]:
                return self.convertLetter(self.first[1])
            elif self.first[2] == self.second[2] and self.first[2] == self.third[2]:
                return self.convertLetter(self.first[2])
            # Diagonal
            elif self.first[0] == self.second[1] and self.first[0] == self.third[2]:
                return self.convertLetter(self.first[0])
            elif self.first[2] == self.second[1] and self.first[2] == self.third[0]:
                return self.convertLetter(self.first[2])
            else:
                return 0
        else:
            return "Tie"

    # Converts string letter on board into it's player (eg. "X" would return 2)

    @log
    def convertLetter(self, letter):
        if letter == '-':
            return 0
        if letter == 'O':
            return 1
        elif letter == 'X':
            return 2

    @log
    def play(self):
        self.printBoard()
        while self.checkWin() == 0:
            self.chooseSpot()
            self.draw()
            self.switchPlayer()
            self.printBoard()
        if self.checkWin() != "Tie":
            print('Player who won:', self.checkWin())
        else:
            print("Tie Game.")

    @staticmethod
    @log
    def reDraw():
        print("Spot already occupied.")
        tictactoe().chooseSpot()
        tictactoe().draw()

    @staticmethod
    @log
    def printBoard():
        print(*tictactoe().first)
        print(*tictactoe().second)
        print(*tictactoe().third)


        # print(f "{tictactoe().first}\n{tictactoe().second}\n{tictactoe().third}")
game = tictactoe()
game_funcs = {"print": game.printBoard,
              "choose": game.chooseSpot,
              "draw": game.draw,
              "switch": game.switchPlayer,
              "exit": "Good bye!"}


@log
def printMenu():
    menu = "".join([f"{select_num+1}. {description}\n" for select_num,
                    description in enumerate(game_funcs)])
    print("\n"+menu)


@log
def select():
    selection = int(input("Choose number: "))
    return selection


@log
def play_manually():
    NUM_OPTIONS = len(game_funcs)
    OPTION_RANGE = range(1, NUM_OPTIONS+1)
    selection = None
    select_is_exit = None

    @log
    def update_selection():
        nonlocal selection, select_is_exit
        selection = select()
        select_is_exit = selection == NUM_OPTIONS

    print("\n---Welcome to the game of Manual TicTacToe!---\n")
    while True:
        printMenu()
        update_selection()
        # repeat if selection not in range
        while selection not in OPTION_RANGE:
            update_selection()
        if select_is_exit:
            print("\n\nGoodbye!")
            break
        # not sure if a for loop is the best way to convert selection to key...
        for option, description in enumerate(game_funcs, start=1):
            if option == selection:
                game_funcs[description]()


play_manually()
# tictactoe().play()
