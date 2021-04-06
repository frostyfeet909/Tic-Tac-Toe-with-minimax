from random import randint, choice
from math import inf
from TicTacToe.bots import player


class Random_Bot(player.Player):
    """
    A bot that makes random moves
    """

    def __init__(self, symbol, opponent, name="Random Bot"):
        """
            name - Name of the player : String
            symbol - Symbol to play with : String
            opponent - Symbol to play against : String
        """
        player.Player.__init__(self, name, symbol, opponent)

    def get_move(self, board):
        """
        Work out the randomest move
            board - The current board : Board
            position - The position to move to : Tuple len == 2
            board -> position
        """
        return choice(board.get_moves())


class Minimax_Bot(player.Player):
    """
    A bot that makes moves based on the minimax algorithm
    """

    def __init__(self, symbol, opponent, name="Minimax Bot", depth=9):
        """
            name - Name of the player : String
            symbol - Symbol to play with : String
            opponent - Symbol to play against : String
            depth - Depth of the minimax search : Integer > 0
        """
        self.depth = depth
        player.Player.__init__(self, name, symbol, opponent)

    def get_move(self, board):
        """
        Work out the minimaximest move
            board - The current board : Board
            position - The position to move to : Tuple len == 2
            board -> position
        """

        # Make a move and work out it's subsequent value
        moves_dict = {}
        for move in board.get_moves():
            board.move(move, self.symbol)
            moves_dict[move] = self.minimax(board, maximizing=False)
            board.undo()

        # Work out the best moves and randomly choose ones
        best_move = max(moves_dict, key=moves_dict.get)
        best_moves = []
        for position in moves_dict.keys():
            if moves_dict[position] >= moves_dict[best_move]:
                best_moves.append(position)

        print(moves_dict)
        # print(best_moves)
        return choice(best_moves)

    def minimax(self, board, depth=inf, alpha=-inf, beta=inf, maximizing=True):
        """
        Use the minimax algorithm with alpha-beta pruning to work out a heuristic value for the current position
            board - The current board : Board
            depth - Current depth of the algorithm : Integer
            alpha : Float
            beta : Float
            maximizing - Is the algorithm maximizing or minimizing the move : Boolean
            value - Value of the current position : Float
            board, depth, alpha, beta, maximizing -> value
        """

        # At max depth set to pre-defined level
        if depth == inf:
            depth = self.depth

        # Return value at end of search
        if depth == 0 or board.finished != None:
            # if board.finished != None:
            # print(depth)
            # board.print_board()
            return board.value_player(self.symbol)

        # My move
        if maximizing:
            value = -inf
            for move in board.get_moves():
                board.move(move, self.symbol)
                value = max(value, self.minimax(
                    board, depth-1, alpha, beta, False))
                board.undo()
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value

        # Their move
        else:
            value = inf
            for move in board.get_moves():
                board.move(move, self.opponent)
                value = min(value, self.minimax(
                    board, depth-1, alpha, beta))
                board.undo()
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value
