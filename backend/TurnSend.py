import json
from json import JSONEncoder

from backend import ChangeTurn, Board
from backend.SquareChange import SquareChange


class TurnSend:
    def __init__(self, listOfSquareChanges, generalChanges):
        self.generalChanges = generalChanges
        self.listOfSquareChanges = listOfSquareChanges


# here json part
class TurnEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def TurnEncoderFunction(turn):
    return TurnEncoder().encode(turn)

board = Board.Board(30, 4)
turn1 = ChangeTurn.ChangeTurn(board, 1, [(1, 1), (2, 2), (3, 3), (4, 4)], {0: 1, 1: 2, 2: 3, 3: 4}, {0: [(1, 1), (2, 2)], 1: [(3, 3), (4, 4)]}, {0: [(5, 5), (6, 6)], 1: [(7, 7), (8, 8)]}, [0, 1])
turn2 = ChangeTurn.ChangeTurn(board, 2, [(1, 1), (2, 2), (3, 3), (4, 4)], {0: 1, 1: 2, 2: 3, 3: 4}, {0: [(1, 1), (2, 2)], 1: [(3, 3), (4, 4)]}, {0: [(5, 5), (6, 6)], 1: [(7, 7), (8, 8)]}, [0, 1])
l = [TurnEncoderFunction(turn1), TurnEncoderFunction(turn2)]
print(l)
