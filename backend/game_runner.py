
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3
MOVE_RIGHT = 4

import random
import closing_area_algorithms


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

        self.collect_players_area(board, players_NPIA)  # also updates some half acptured

        self.handle_cuts(players_NPIA)

        self.handle_kills(board, players_NPIA)

        self.update_positions(board, players_NPIA)

        self.add_new_keys(board)





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

    # todo: nice to have, two players may close the same area in the same time, currently this is
    # todo: arbitrary, but maybe later implement that the one that closes the bigger area takes it

    def collect_players_area(self, board, players_NPIA):
        for player_index in range(len(players_NPIA)):
            self.collect_player_area(board, player_index, players_NPIA)


    def collect_player_area(self, board, player_index, players_NPAI):
        player = board.players[player_index]
        if closing_area_algorithms.has_closed(player, board.SIZE, players_NPAI[player_index]):
            new_area_dictionary = closing_area_algorithms.get_union_area(board.SIZE, player.halfCaptured, player.area)
            new_area = [pos for pos in new_area_dictionary.keys() if new_area_dictionary[pos] == 0]
            new_area = [pos for pos in new_area if (0 <= pos[0] < board.SIZE and 0 <= pos[1] < board.SIZE)]
            new_area = new_area + player.area # it may be that not all player.area is in new_area
            new_area = list(set(new_area))

            added_area = [pos for pos in new_area if pos not in player.area]

            player.area = new_area

            # removing added area from others:
            for other_player in board.players:
                if other_player != player:
                    for pos in added_area:
                        other_player.area.remove(pos)
                        if pos in other_player.keysPositions:
                            other_player.keysPositions.remove(pos)
                            player.keysPositions.append(pos)

            player.halfCaptured = []

        elif players_NPAI[player_index] not in player.area:
            # need to add to half captured

            # if now started bondry, add the last pos in the area
            if player.position in player.area:
                player.halfCaptured.append(player.position)

            player.halfCaptured.append(players_NPAI[player_index])

        else:
            # player in its area, and not after closing area
            # need this in case entered differnet connected area after was out of its area
            player.halfCaptured = []


    # check that did this: when collecting area, also update half captured
    # check that did this: also add NPAI to half captured
    # check that did this: also check if moved to different area, and make the half captured empty if yes


    def handle_cuts(self, players_NPAI):
        for player_index in range(len(players_NPAI)):
            player = board.players[player_index]
            if self.is_player_cut(player, players_NPAI)
                self.cut_player(board, player_index)


    # assuming it was not killed
    def is_player_cut(self, player, players_NPAI):
        for other_player_index in range(len(players_NPAI)):
            # note that we also check if the player cuts iself

            # check if other player cuts player:
            if players_NPAI[other_player_index] in player.halfCaptured:
                return True
        return False


    def cut_player(self, board, player_index):
        # notice that if the player is not killed, it still has its gate
        player = board.players[player_index]

        player.position = player.gate_pos
        player.halfCaptured = []
        # notice that the gate does not contain keys

    # returns a list of (player_index1, player_index2) such that player 1 killed player 2
    def get_killed_tuples(self, board, players_NPIA):

        tried_kills = []

        for player_index in range(len(players_NPIA)):
            player_gate_pos = board.players[player_index].gate_pos

            for other_player_index in range(len(players_NPIA)):
                if other_player_index != player_index:
                    if players_NPIA[other_player_index] == player_gate_pos:
                        # means the other player was going to be be in the player's gate
                        tried_kills.append((other_player_index, player_index))

        # check if two players try to kill each other (it matters if they have the same number of keys):
        for player_index1 in range(len(players_NPIA)):
            for player_index2 in range(len(players_NPIA)):
                if player_index1 != player_index2:
                    if (player_index1, player_index2) in tried_kills and (player_index2, player_index1) in tried_kills:
                        tried_kills.remove((player_index1, player_index2))
                        tried_kills.remove((player_index2, player_index1))

                        # it does not matter if they have the same keys or not, adding the following
                        # random couple should be okay

                        if random.random() < 0.5:
                            tried_kills.append((player_index1, player_index2))
                        else:
                            tried_kills.append((player_index1, player_index2))

        # not every kill is well decided acording to the number of keys

        kills = []
        for tried_kill in tried_kills:
            player1 = board.players[tried_kill[0]]
            player2 = board.players[tried_kill[1]]

            if player1.keys < player2.keys:
                kills.append((tried_kill[1], tried_kill[0]))
            else:
                kills.append(tried_kill)

        # todo: add so that there won't be cycles (by randomness)

        # check for players that killed and were kills:

        changed_kills = True # until the check does not change the kills
        while changed_kills:
            changed_kills = False
            kills_tuple = None
            for kill1 in kills:
                for kill2 in kills:
                    if kill1 != kill2:
                        if kill1[1] == kill2[0]:
                            changed_kills = True
                            kills_tuple = (kill1, kill2)
            if kills_tuple != None:
                kills.remove(kills_tuple[0])
                kills.remove(kills_tuple[1])
                kills.append((kills_tuple[0][0], kills_tuple[1][1]))

        return kills


    def handle_kill_tuple(self, board, did_kill_index, got_killed_index):

        did_kill = board.players[did_kill_index]
        got_killed = board.players[got_killed_index]

        if got_killed.is_alive:  # todo: improve by dealing with these in getting kills tuples
            got_killed.is_alive = False

            did_kill.area = did_kill.area + got_killed.area
            did_kill.area = list(set(did_kill.area))  # to make sure

            did_kill.halfCaptured = []

            did_kill.keys = did_kill.keys - got_killed.keys

            # now changing board:

            board.players.remove(got_killed)
            board.numOfPlayers = len(board.players)


    def handle_kills(self, board, players_NPIA):
        for kill in self.get_killed_tuples(board, players_NPIA):
            self.handle_kill_tuple(kill)


    def update_positions(self, board, players_NPAI):
        for player_index in range(len(players_NPAI)):
            player = board.players[player_index]

            last_pos = player.position

            player.position = players_NPAI[player_index]
            pos = player.position

            # need to update last_move from last_pos to pos:

            if pos[1] == last_pos[1] + 1:
                last_move = MOVE_DOWN
            elif pos[0] == last_pos[0] - 1:
                last_move = MOVE_LEFT
            elif pos[1] == last_pos[1] - 1:
                last_move = MOVE_UP
            elif pos[0] == last_pos[0] + 1:
                last_move = MOVE_RIGHT
            else: # means the player did not move
                last_move = player.last_move

            player.last_move = last_move


    def add_new_keys(self, board):
        r=random.randint(1,board.Size*board.Size)
        for player in board.players:
            if len(player.area)>=r:
                relevantBlocks=[]
                for block in player.area:
                    cond=0
                    for p in board.players:
                        if block == p.position:
                            cond=1
                    if not (block in player.keysPositions or player.gate_pos==block or cond==1):
                        relevantBlocks.append(block)
                if len(relevantBlocks)>0:
                    ra=random.randint(0,len(relevantBlocks)-1)
                    player.keysPositions.append(relevantBlocks[ra])


    def is_legal_move(self, player_move):
        return player_move in [MOVE_DOWN, MOVE_LEFT, MOVE_UP, MOVE_RIGHT]


# if move is


# todo: adding the keys
# todo: time until game is over
# todo: keys are not in the gates
# todo: remove from board the killed players
# todo: key not in gate

# todo: add keys in the end, of alive players and in positions where no one are
# todo: update all the fields in all of the classes


