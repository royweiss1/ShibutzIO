class SquareChange:
    def __init__(self, xPos, yPos, playerIndex, status):
        self.xPosition = xPos
        self.yPosition = yPos
        self.playerIndex = playerIndex #playerIndex, 0 - natural
        self.Status = status # 0 - natural, 1 - player, 2 - half, 3 - full, 4 - key
