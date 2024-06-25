from decks import get_decks


class GameMaster:
    def __init__(self):
        self._players = []
    # todo create player

    def add_player(self, player):
        # todo verify player
        if len(self._players) > 3:
            raise ValueError("Too many players in this game")
        # optional many players, 4 in one game
        self._players.append(player)

    def is_ready(self):
        if len(self._players) == 4:
            return True
        else:
            pass
            # todo some kind of error

    def prepare_players(self):
        decks = get_decks()
        for i in range(4):
            player = self._players[i]
            player.set_deck(decks[i])
            self._players[i] = player

    def game_start(self):
        if self.is_ready():
            self.prepare_players()

    def get_players(self):
        for player in self._players:
            print(player)
