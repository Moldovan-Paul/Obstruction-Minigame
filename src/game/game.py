import copy
from enum import Enum


class GameException(Exception):
    pass

class Game:
    def __init__(self, board):
        self.__board = board

    def get_board(self):
        return self.__board.board

    def is_game_over(self):
        """
        Returns current game state
        """
        if self.__board.is_board_won():
            return 1
        return 0

    def make_move_player(self, x, y):
        """
        Marks a position on the board as occupied by the human player if possible
        :param x: X axis index
        :param y: Y axis index
        """
        if not self.__board.indices_in_range(x,y):
            raise GameException("Position is not valid")
        if self.__board.get_board_pos(x,y) == '-':
            self.__board.set_board_pos(x,y, 'X')
        else:
            raise GameException("Territory is occupied")
        self.__board.make_border(x,y)


    def make_move_computer(self):
        """
        Calculates and executes best move that computer can make in order to win
        """
        best_score = -1000
        best_position_row = 10
        best_position_column = 10
        for row in range(6):
            for column in range(6):
                if self.__board.get_board_pos(row, column) == '-':
                    self.__board.set_board_pos(row, column, 'O')
                    self.__board.make_border(row, column)
                    score = self.minimax(0)
                    self.__board.set_board_pos(row, column, '-')
                    self.__board.clear_border(row, column)
                    if score > best_score:
                        best_score = score
                        best_position_row = row
                        best_position_column = column
        self.__board.set_board_pos(best_position_row, best_position_column, 'O')
        self.__board.make_border(best_position_row, best_position_column)

    def minimax(self, is_maximizing):
        """
            Algorithm which evaluates all possible outcomes of a board state by continuing the game against itself.
        When an game over state is reached, if the computer won, a score of 1 will be assigned to the last move, or -1
        otherwise. While tracing back on the stack of execution, a score of 1 or -1 will be assigned to a move based
        on whether it is the 'O' player's turn or the 'X' player's turn. 'O' will choose 1 if possible and 'X' will
        choose -1 if possible. In the end, the computer will choose the first move which has a positive evaluated
        outcome.
        :param is_maximizing: 'X' or 'O' player's turn (0/1)
        """
        if self.__board.is_board_won():
            if is_maximizing:
                return 1
            else:
                return -1

        if is_maximizing:
            best_score = -2
            for row in range(6):
                for column in range(6):
                    if self.__board.get_board_pos(row, column) == '-':
                        self.__board.set_board_pos(row, column, 'O')
                        self.__board.make_border(row, column)
                        score = self.minimax(0)
                        self.__board.set_board_pos(row, column, '-')
                        self.__board.clear_border(row, column)
                        best_score = max(score, best_score)
                return best_score
        else:
            best_score = 2
            for row in range(6):
                for column in range(6):
                    if self.__board.get_board_pos(row, column) == '-':
                        self.__board.set_board_pos(row, column, 'X')
                        self.__board.make_border(row, column)
                        score = self.minimax(1)
                        self.__board.set_board_pos(row, column, '-')
                        self.__board.clear_border(row, column)
                        best_score = min(score, best_score)
                return best_score

