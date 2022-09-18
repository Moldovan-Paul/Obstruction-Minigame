from board.board import Board
from game.game import Game
from ui.ui import Console

board = Board()
game = Game(board)
console = Console(game)

console.run()