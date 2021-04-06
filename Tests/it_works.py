from sys import path


def main():
    import TicTacToe as tm
    import TicTacToe.bots as tm_bots

    bot_minmax = tm_bots.Minimax_Bot("x", "o", "Bob")
    bot_random = tm_bots.Random_Bot("o", "x", "Bill")

    game = tm.Game([bot_minmax, bot_random])
    game.run()


if __name__ == "__main__":
    path.insert(1, './')  # Add ../ to path
    main()
