

# returns pos to expand to if exists, or None otherwise
def get_to_expand_to(board_size, pos, same_type_predicate):
    max_board_index = board_size - 1

    # left
    if pos[0] > 0 and same_type_predicate((pos[0] - 1, pos[1])):
        return pos[0] - 1, pos[1]
    # right
    if pos[0] < max_board_index and same_type_predicate(pos[0] + 1, pos[1])
        return pos[0] + 1, pos[1]
    # up
    if pos[1] > 0 and same_type_predicate(pos[1])

def expand(board_size, pos, same_type_predicate):




def get_connected_components(board_size, area):


