MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3
MOVE_RIGHT = 4

class Board:
    def __init__(self, size, numPlayers):
        self.size = size
        self.numPlayers = numPlayers
        self.players = []
        self.turn = 0
    
class Player:
    def __init__(self, position):
        self.position = position
        self.area = []
        self.halfCaptured = []
        self.keys = 0
        self.keysPositions = []
        self.is_alive = True
        self.last_move = 1
        self.gate_pos = position

def distance(pos1, pos2):
    return abs((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def get_area_outline(board):
    # get the outline of the area of player 0
    area = board.players[0].area
    outline = []
    for point in area:
        if (point[0]+1, point[1]) not in area:
            outline.append(point)
        if (point[0]-1, point[1]) not in area:
            outline.append(point)
        if (point[0], point[1]+1) not in area:
            outline.append(point)
        if (point[0], point[1]-1) not in area:
            outline.append(point)

def get_closest_outline(position, area):
    closest = None
    for point in get_area_outline(area):
        if closest == None:
            closest = point
        else:
            if distance(position, point) < distance(position, closest):
                closest = point
    return closest

def move_to_side(last_turn):
        if last_turn == 1:
            return 2
        if last_turn == 2:
            return 1
        if last_turn == 3:
            return 4
        if last_turn == 4:
            return 3
        
def move_to_oppsite(last_turn):
    if last_turn == 1:
        return 3
    if last_turn == 2:
        return 4
    if last_turn == 3:
        return 1
    if last_turn == 4:
        return 2

def is_in_area(self, position, area):
    for point in area:
        if position == point:
            return True
    return False

def get_closest_out_of_outline(self, position ,area):
    closest_outline = get_closest_outline(position, area)
    if not self.is_in_area((closest_outline[0]+1, closest_outline[1]), area):
        return (closest_outline[0]+1, closest_outline[1])
    if not self.is_in_area((closest_outline[0]-1, closest_outline[1]), area):
        return (closest_outline[0]-1, closest_outline[1])
    if not self.is_in_area((closest_outline[0], closest_outline[1]+1), area):
        return (closest_outline[0], closest_outline[1]+1)
    if not self.is_in_area((closest_outline[0], closest_outline[1]-1), area):
        return (closest_outline[0], closest_outline[1]-1)
