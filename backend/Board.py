from backend import Player

DEFAULT_LOCATION = {2: [], 4: [[0,0], [0,29] , [29,0], [29,29]]}


class Board:
    def __init__(self, size, numPlayers):
        self.SIZE = size
        self.numOfPlayers = numPlayers
        self.players = []  # to init
        index=0
        for i in DEFAULT_LOCATION[numPlayers]:
            self.players.append(Player.Player(i, index))
            index+=1

    def whoOwns(self, position):
        pass
    def isKey(self, position):
        pass

    def getPlayerArea(self, playerIndex):
        pass

