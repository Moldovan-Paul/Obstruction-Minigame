import unittest

from board.board import Board
from src.game.game import Game, GameException


class GameTests(unittest.TestCase):

    def setUp(self) -> None:
        """
        Runs before every test method
        """
        board = Board()
        game = Game(board)

        self._board = board
        self._game = game

    def test_make_move_player(self):
        self._game.make_move_player(2,3)
        self.assertEqual(self._board.board, "-  -  -  -  -  -  \n-  -  +  +  +  -  \n-  -  +  X  +  -  \n-  -  +  +  +  -  \n"
                                            "-  -  -  -  -  -  \n-  -  -  -  -  -  \n")
        with self.assertRaises(GameException) as ge:
            self._game.make_move_player(2, 3)
        self.assertEqual(str(ge.exception), "Position is occupied")
        with self.assertRaises(GameException) as ge:
            self._game.make_move_player(10, 10)
        self.assertEqual(str(ge.exception), "Position is not valid")
