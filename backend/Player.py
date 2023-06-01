from backend import game_runner

class Player:
    def __init__(self, position, playerIndex):
        self.playerIndex = playerIndex
        self.position = position #pair x,y
        self.area = [] #list of coordinats of area
        self.halfCaptured = [] # by order of capture, always not None
        self.keys = 0 #num of keys
        self.keysPositions = [] #
        self.is_alive = True
        self.last_move = game_runner.MOVE_UP
        self.gate_pos = position





