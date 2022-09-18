import unittest

from board import Board
from game.game import Game


class GameTests(unittest.TestCase):

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        board = Board()
        game = Game(board)

        self._board = board
        self._game = game

    def test_to_string(self):
        self.assertEqual(self._board.board, "-  -  -  -  -  -  \n-  -  -  -  -  -  \n-  -  -  -  -  -  \n-  -  -  -  -  -  \n"
                                            "-  -  -  -  -  -  \n-  -  -  -  -  -  \n")

    def test_is_board_won(self):
        for i in range(6):
            for j in range(6):
                if self._board.get_board_pos(i,j) == '-':
                    self._board.set_board_pos(i,j, 'X')
        self.assertEqual(self._board.is_board_won(), 1)
        self._board.set_board_pos(2,3, '-')
        self.assertEqual(self._board.is_board_won(), 0)

    def test_make_border(self):
        self._board.make_border(2,3)
        self.assertEqual(self._board.board, "-  -  -  -  -  -  \n-  -  +  +  +  -  \n-  -  +  -  +  -  \n-  -  +  +  +  -  \n"
                         "-  -  -  -  -  -  \n-  -  -  -  -  -  \n")
        self._board.make_border(0,0)
        self.assertEqual(self._board.board, "-  +  -  -  -  -  \n+  +  +  +  +  -  \n-  -  +  -  +  -  \n-  -  +  +  +  -  \n"
                         "-  -  -  -  -  -  \n-  -  -  -  -  -  \n")

    def test_clear_border(self):
        self._board.set_board_pos(2,3, 'X')
        self._board.make_border(2, 3)
        self._board.clear_border(2,3)
        self.assertEqual(self._board.board, "-  -  -  -  -  -  \n-  -  -  -  -  -  \n-  -  -  X  -  -  \n-  -  -  -  -  -  \n"
                         "-  -  -  -  -  -  \n-  -  -  -  -  -  \n")