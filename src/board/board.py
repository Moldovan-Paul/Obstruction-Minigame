
class Board:
    def __init__(self):
        self.__board = [['-','-','-','-','-','-'],
                        ['-','-','-','-','-','-'],
                        ['-','-','-','-','-','-'],
                        ['-','-','-','-','-','-'],
                        ['-','-','-','-','-','-'],
                        ['-','-','-','-','-','-']]

    def to_string(self):
        """
        Converts board to a printable string
        """
        result = ""
        for row in range(6):
            for column in range(6):
                result += self.get_board_pos(row, column)
                result += "  "
            result += '\n'
        return result

    def is_board_won(self):
        """
        Checks whether current game is finished or can be continued
        :return: True if finished, false otherwise
        """
        for i in range(6):
            for j in range(6):
                if self.__board[i][j] == '-':
                    return False
        return True

    def make_border(self, x, y):
        """
        Marks area around a new marked position as unavailable
        """
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if self.indices_in_range(i,j) and not (i == x and j == y):
                    self.__board[i][j] = '+'

    def clear_border(self, x, y):
        """
        Clears border formed around a position (for minimax algorithm)
         """
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.indices_in_range(i, j) and not (i == x and j == y):
                    ok = 1
                    for ii in range(i-1, i+2):
                        if ok == 0:
                            break
                        for jj in range(j-1, j+2):
                            if self.indices_in_range(ii, jj) and not (ii == x and jj == y):
                                if self.get_board_pos(ii, jj) == 'X' or self.get_board_pos(ii, jj) == 'O':
                                    ok = 0
                                    break
                    if ok:
                        self.__board[i][j] = '-'

    def get_board_pos(self, x, y):
        return self.__board[x][y]

    def set_board_pos(self, x, y, value):
        self.__board[x][y] = value

    def get_board_values(self):
        """
        Returns board as usable list of lists
        """
        return self.__board

    @property
    def board(self):
        """
        Returns board as printable string
        """
        return self.to_string()

    @staticmethod
    def indices_in_range(x, y):
        """
        Checks whether given indices are a position on the board
        """
        if x<6 and x>-1 and y<6 and y>-1:
            return True
        return False