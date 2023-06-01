import json

from backend.SquareChange import SquareChange
HEAD = 1
TAIL = 2
FULL = 3
KEY = 4
NATURAL = 0

class ChangeTurn:
    def __init__(self, board, turnIndex, playersNewPosition, score, newCapturedArea=None, newHalfCapturedArea=None, newKilled=None):
        self.turnIndex = turnIndex
        board = board
        self.Score = score # playerIndex to newScore
        playersNewPosition = playersNewPosition  # list of x,y changes in players position => index is player index

        if newCapturedArea is None:
            newCapturedArea = {}
        else:
            newCapturedArea = newCapturedArea # playerIndex to list of coordinats of new fully captured
        if newHalfCapturedArea is None:
            newHalfCapturedArea = {}
        else:
            newHalfCapturedArea = newHalfCapturedArea #playerIndex to ...
        if newKilled is None:
            newKilled = []
        else:
            newKilled = newKilled #list of playerIndex

        self.SquareChanges = []
        if newCapturedArea is not None:
            for player in newCapturedArea:
                for square in newCapturedArea[player]:
                    key = board.isKey(square)
                    if key:
                        self.SquareChanges.append(SquareChange(square[0], square[1], player, KEY))
                    else:
                        self.SquareChanges.append(SquareChange(square[0], square[1], player, FULL))
        if newHalfCapturedArea is not None:
            for player in newHalfCapturedArea:
                for square in newHalfCapturedArea[player]:
                    key = board.isKey(square) # probably False
                    if key:
                        self.SquareChanges.append(SquareChange(square[0], square[1], board.whoOwns(square), KEY))
                    else:
                        self.SquareChanges.append(SquareChange(square[0], square[1], player, TAIL))
        for player in range(len(playersNewPosition)):
            key = board.isKey(playersNewPosition[player])  # probably False MIND
            self.SquareChanges.append(SquareChange(playersNewPosition[player][0], playersNewPosition[player][1], player, HEAD))
        #for playerIndex in newKilled:
        #    for square in board.getPlayerArea(playerIndex):
        #        SquareChanges.append(SquareChange(square[0], square[1], NATURAL, NATURAL))

        #for player in score:
        #    self.Score["Score"].append({"Player": player, "Score": Score[player]})

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



