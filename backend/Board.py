import Player

DEFAULT_LOCATION = {2: [], 4: []}


class Board:
    def __init__(self, size, numPlayers):
        self.SIZE = size
        self.numOfPlayers = numPlayers
        self.players = []  # to init
        for i in DEFAULT_LOCATION[numPlayers]:
            self.players.append(Player.Player(i))


