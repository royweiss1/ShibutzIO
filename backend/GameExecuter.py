import os


def makeFile(code, playerIndex):
    filename = 'player' + str(playerIndex) + '.py'
    file_path = 'players_files/'
    # Combine the file path and filename
    full_path = os.path.join(file_path, filename)
    # Create the directory if it doesn't exist
    os.makedirs(file_path, exist_ok=True)
    # Write the code to the new file
    with open(full_path, 'w') as file:
        file.write(code)


class Runner:
    def __init__(self, board, playerId):
        self.board = board
        self.playerId = playerId
        self.player = None

    def load_player_bot(self, file_path):
        with open(file_path, 'r') as file:
            code = file.read()

        global_vars = {}
        exec(code, global_vars)

        player_bot_class = global_vars.get('Survivor')  # MIND THE NAME
        if player_bot_class:
            self.player = player_bot_class()
        else:
            raise Exception("PlayerBot class not found in the provided file.")

    def run_game_turn(self):
        if self.player:
            return self.player.make_turn(self.board, self.playerId)
        else:
            raise Exception("PlayerBot not loaded.")


# Usage
def run(board):
    runnersList = []
    for i in range(4):
        runner = Runner(board, i)
        runner.load_player_bot("players_files/player" + str(i) + ".py")
        runnersList.append(runner)
    playersActions = []  # index to action
    for runner in runnersList:
        playersActions.append(runner.run_game_turn())
    return playersActions


def makeFiles(listOfPlayersCode):
    for i in range(4):
        makeFile(listOfPlayersCode[i], i)
