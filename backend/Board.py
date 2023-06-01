import Player
import importlib

DEFAULT_LOCATION = {2: [], 4: []}


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
        if position is [1,1]:
            return True

    def getPlayerArea(self, playerIndex):
        pass

