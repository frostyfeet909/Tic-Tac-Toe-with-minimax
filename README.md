# Tic Tac Toe with Minimax

A text based implementation of tic tac toe, where you can play against a bot using the minimax algorithm.

## Installation

No additional requirements are needed apart from the lastest [python3](https://www.python.org/downloads/).

## Usage

```python
import TicTacToe as tm
import TicTacToe.bots as tm_bots

bot_minmax = tm_bots.Minimax_Bot("x", "o", "Bob")
bot_random = tm_bots.Random_Bot("o", "x", "Bill")

game = tm.Game([bot_minmax, bot_random])
game.run()
# Starts a game with one bot playing random moves and the other using the minimax algorithm
```

## License

me no know
