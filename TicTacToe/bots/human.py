from TicTacToe.bots import player


class Human(player.Player):
    """
    A text based human player
    """

    def __init__(self, symbol, opponent, name="Human"):
        """
            name - Name of the player : String
            symbol - Symbol to play with : String
            opponent - Symbol to play against : String
        """
        Player.__init__(self, name, symbol, opponent)

    def get_move(self, board):
        """
        Get the move from the human
            board - The current board : Board
            position - The position to move to : Tuple len == 2
            board -> position
        """
        print("Player %s what is your move:" % self.name)
        position = (input("i: "), input("j: "))

        return position
