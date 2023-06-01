
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3
MOVE_RIGHT = 4


class GameRunner:
    def __init__(self):
        # todo: initialize history
        self.history = None

    # players_moves: only for living players
    # todo: return board
    def update(self, board, players_moves):
        if len(players_moves) != len(board.players):
            raise Exception  # this should not happen

        self.check_legal_moves(board, players_moves) # converting illegal moves to last moves
        
        # all moves are legal
        
        players_NPIA = self.get_players_NPIA(board, players_moves)  # NPIA: new position if alive
        
        self.collect_players_existing_keys(board, players_NPIA)
        

    # converts non legal moves to legal moves
    def check_legal_moves(self, board, players_moves):
        for player_index in range(len(players_moves)):
            if not self.is_legal_move(players_moves[player_index]):
                players_moves[player_index] = board.players[player_index].last_move

    def get_players_NPIA(self, board, players_moves):
        return [self.get_player_NPIA(board, players_moves, player_index) for player_index in range(len(players_moves))]

    # NPIA - new position if alive (and not cut), None means not alive, but its not if and only if
    def get_player_NPIA(self, board, players_moves, player_index):
        last_pos = board.players[player_index].position
        move = players_moves[player_index]
        max_pos_value = board.SIZE - 1

        if move == MOVE_UP:
            if last_pos[1] == 0:
                return last_pos
            else:
                return last_pos[0], last_pos[1] - 1
        elif move == MOVE_DOWN:
            if last_pos[1] == max_pos_value:
                return last_pos
            else:
                return last_pos[0], last_pos[1] + 1
        elif move == MOVE_LEFT:
            if last_pos[0] == 0:
                return last_pos
            else:
                return last_pos[0] - 1, last_pos[1]
        elif move == MOVE_RIGHT:
            if last_pos[0] == max_pos_value:
                return last_pos
            else:
                return last_pos[0] + 1, last_pos[1]

        # should not get here because assuming already converted to legal pos
        raise Exception


    def collect_players_existing_keys(self, board, players_NPIA):
        for player_index in range(len(players_NPIA)):
            player = board.players[player_index]
            new_pos = players_NPIA[player_index]

            if new_pos in player.keysPositions:
                player.keys = player.keys + 1
                player.keysPositions.remove(new_pos)

    def collect_players_area(self):
        pass

    def did_close_area(self, board, players_NPIA, player_index):
        player = board.players[player_index]
        last_pos = player.position
        NPAI = players_NPIA[player_index]

        return (last_pos not in player.area) and (NPAI in player.area)


    # assuming it was not killed
    def is_player_cut(self):
        pass

    # notice two playes can not kill each other in the same turn
    def is_player_killed(self, board, players_NPIA, player_index):
        player_gate_pos = board.players[player_index].gate_pos

        for other_player_index in range(len(players_NPIA)):
            if other_player_index != player_index:
                if players_NPIA[other_player_index] == player_gate_pos:
                    # means the other player will be in the player's gate
                    # todo: continue this

    def is_legal_move(self, player_move):
        return player_move in [MOVE_DOWN, MOVE_LEFT, MOVE_UP, MOVE_RIGHT]

# if move is


# todo: adding the keys
# todo: time until game is over
# todo: keys are not in the gates
# todo: remove from board the killed players

# todo: add keys in the end, of alive players and in positions where no one are
# todo: update all the fields in all of the classes


