import GameExecuter
import Board

def main(playerStrategies):
    # initialize game
    GameExecuter.makeFiles(playerStrategies)
    board = Board.Board(10, 4)

    # run game
    for i in range(1000):
        actionsThisTurn=GameExecuter.run() #list of actions
        # do the update stuff -> update board
