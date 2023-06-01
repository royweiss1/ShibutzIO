
class History:
    def __init__(self):
        self.TurnHistory = []

    def addTurn(self, playerIndexToChangeTurn): #?
        for p in playerIndexToChangeTurn:
            self.TurnHistory.append(playerIndexToChangeTurn[p])
