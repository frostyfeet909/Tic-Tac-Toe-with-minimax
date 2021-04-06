class Board:
    """
    Stores a representation of the board, gets valid moves and other game functions
    """

    def __init__(self):
        """
        """
        self.moves = []
        self.finished = None
        self.board = {}
        self._size = 3
        self.setup_board()

    def reset(self):
        """
        Reset the whole board
        """
        self.moves = []
        self.finished = None
        self.setup_board()

    def setup_board(self):
        """
        Empty the board
        """
        for i in range(1, self._size+1):
            for j in range(1, self._size+1):
                self.board[(i, j)] = " "

    def move(self, position, symbol):
        """
        Bust a move
            position - Position of the move : Tuple len == 2
            symbol - The symbol to make a move : String
            position, symbol -> Boolean
        """

        # Weak validation
        if not (1 <= (position[0] and position[1]) <= self._size):
            print("Bad move")
            return False

        # Bust a move if the square is empty
        if self.board[position] == " ":
            self.moves.append(position)
            self.board[position] = symbol

            # If no-one won then check if the board is full
            if not self.check_win(position, symbol):
                self.check_full()
            return True

        return False

    def undo(self):
        """
        Undo the last move
        """
        last_move = self.moves.pop()
        symbol = self.board[last_move]
        self.board[last_move] = " "

        # If no-one won then check if the board is full. if the board isn't full then the game isnn't finished
        if not self.check_win(last_move, symbol):
            if not self.check_full():
                self.finished = None

    def get_moves(self):
        """
        Get valid moves to be made
            moves - List of valid positions to move : Array
            -> moves
        """
        moves = []
        for position in self.board.keys():
            if self.board[position] == " ":
                moves.append(position)

        return moves

    def value_player(self, symbol):
        """
        Value the given players position
            symbol - The symbol to make a move : String
            value - The value of the player : Float
            symbol -> value
        """
        if self.finished == (None or " "):
            # Draw and transient states are worth nothing
            value = 0.0
        # +/- the no. of moves to make faster wins/losses more important
        elif self.finished == symbol:
            value = 10.0 - len(self.moves)
        else:
            value = -10.0 + len(self.moves)

        return value

    def check_win(self, position, symbol):
        """
        Check if the last player to move has won
            position - Position of the move : Tuple len == 2
            symbol - The symbol to make a move : String
            position, symbol -> Boolean
        """
        # Horizontal?
        if all(self.board[(position[0], i)] == symbol for i in range(1, self._size+1)):
            self.finished = symbol
            return True

        # Vertical?
        if all(self.board[(i, position[1])] == symbol for i in range(1, self._size+1)):
            self.finished = symbol
            return True

        # Leading diagonal
        if position[0] == position[1]:
            if all(self.board[(i, i)] == symbol for i in range(1, self._size+1)):
                self.finished = symbol
                return True

        # Other diagonal
        if position[0] == position[1] or position[0]+self._size-1 == position[1] or position[0] == position[1]+self._size-1:
            if all(self.board[(i, (self._size+1)-i)] == symbol for i in range(1, self._size+1)):
                self.finished = symbol
                return True

        return False

    def check_full(self):
        """
        Check if the board is full and the game is a draw
            -> Boolean
        """
        if len(self.moves) >= 9:
            self.finished = " "
            return True

        return False

    def print_board(self):
        """
        Display the board
        """
        for j in range(1, self._size+1):
            print(" ", end="")
            for i in range(1, self._size+1):
                if i == self._size:
                    ending = ""
                else:
                    ending = " | "

                print(self.board[(i, j)], end=ending)
            print()
            print("  -------")
