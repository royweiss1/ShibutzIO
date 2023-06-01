import json
from json import JSONEncoder

from backend import GameExecuter
from backend import Board
from backend import game_runner

class TurnEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def TurnEncoderFunction(turn):
    return TurnEncoder().encode(turn)

def main(playerStrategies):
    # initialize game
    GameExecuter.makeFiles(playerStrategies) # list of strings
    board = Board.Board(10, 4)
    g=game_runner.GameRunner()
    listofChangeTurn = []

    # run game
    for i in range(1000):
        actionsThisTurn=GameExecuter.run(board) #list of actions
        # do the update stuff -> update board
        ChangeTurn = g.update(board, actionsThisTurn)
        if (len(board.players)) == 1:
            break
        listofChangeTurn.append(ChangeTurn)
    saveToFile(listofChangeTurn)
    return True

def saveToFile(listofChangeTurn):
    # save to file
    l = []
    for i in listofChangeTurn:
        l.append(TurnEncoderFunction(i))
    #json_data = json.dumps(l)
    with open('data.txt', 'w') as outfile:
        outfile.write(str(l))
