from TicTacToe.board import Board
import time
from random import randint


class Game:
    """
    Class to run the game, setup UI, take input
    """

    def __init__(self, players):
        """
            players - List of player objects : Array
        """
        self.board = Board()
        self.players = players
        self.no_players = len(players)

    def run(self, repeats=1, quiet=False):
        """
        Run the game
            repeats - Number of times to repeat the game : Integer > 0
            quiet - Should the board be displayed : Boolean
        """
        print("Welcome to tic tac toe")

        for i in range(1, repeats+1):
            print("Game %i" % i)
            # Random starting player
            next_player = randint(0, self.no_players-1)

            while self.board.finished == None:
                if not quiet:
                    print("Player %s's turn" % self.players[next_player].name)

                # Get player input and make the move
                move = self.players[next_player].get_move(self.board)
                self.board.move(move, self.players[next_player].symbol)

                if not quiet:
                    self.board.print_board()
                # raise SystemExit

                # Go to next player in the list (wraps around)
                next_player = 0 if next_player+1 > self.no_players-1 else next_player+1

            # Credit winner
            winner = None
            for player in self.players:
                if player.symbol == self.board.finished:
                    player.wins += 1
                    winner = player
                    break

            if winner != None:
                print("Player %s has won!" % winner.name)
            else:
                print("No one has won!")

            self.board.reset()

        # Sort players by wins
        self.players.sort(key=lambda x: x.wins, reverse=True)

        print("Finished")
        if self.players[0].wins > 0:
            print("Overall - Player %s has won!" % self.players[0].name)
            print("Leaderboard: ")
            for i in range(0, len(self.players)):
                print("    %i %s : %i" %
                      (i+1, self.players[i].name, self.players[i].wins))
        else:
            print("There were no winners today...")
