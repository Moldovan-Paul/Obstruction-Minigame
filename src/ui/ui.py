from game.game import GameException

class InputException(GameException):
    pass

class Console:
    def __init__(self, game):
        self.__game = game

    def print_board(self):
        print(self.__game.get_board())

    @staticmethod
    def input_player_choice_row():
        position = input("Choose a position on the board (row): ")
        if position.isdigit():
            return position
        else:
            raise InputException("Input must be a number")

    @staticmethod
    def print_player_win():
        print("You won!")

    @staticmethod
    def print_computer_win():
        print("Computer wins!")

    @staticmethod
    def input_player_choice_column():
        position = input("Choose a position on the board (column): ")
        if position.isdigit():
            return position
        else:
            raise InputException("Input must be a number")

    def run(self):
        while True:
            try:
                self.print_board()
                self.__game.make_move_player(int(self.input_player_choice_row()), int(self.input_player_choice_column()))
                if self.__game.is_game_over():
                    self.print_board()
                    self.print_player_win()
                    break
                self.__game.make_move_computer()
                if self.__game.is_game_over():
                    self.print_board()
                    self.print_computer_win()
                    break

            except GameException as ge:
                print(str(ge))
