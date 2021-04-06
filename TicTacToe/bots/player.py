class Player:
    """
    Base/Abstract class for the bots/human players
    """

    def __init__(self, name, symbol, opponent):
        """
            name - Name of the player : String
            symbol - Symbol to play with : String
            opponent - Symbol to play against : String
        """
        self.name = name
        self.wins = 0
        self.symbol = symbol
        self.opponent = opponent

    def get_move(self, board):
        """
        Work out the best move
            board - The current board : Board
            position - The position to move to : Tuple len == 2
            board -> position
        """
        return None
