import GameExecuter
import Board
from backend import game_runner


def main(playerStrategies):
    # initialize game
    GameExecuter.makeFiles(playerStrategies) # list of strings
    board = Board.Board(10, 4)
    g=game_runner.GameRunner()

    # run game
    for i in range(1000):
        actionsThisTurn=GameExecuter.run(board) #list of actions
        # do the update stuff -> update board
        ChangeTurn = g.update(board, actionsThisTurn)
