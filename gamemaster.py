from player import Player
from decks import get_decks

class Gamemaster:
    def __init__(self):
        self._players = []
    # todo create player
    def add_player(self, player):
        # todo weryfikacja poprawnosci player
        if len(self._players) > 3:
            raise ValueError("Too many players in this game")
        # optional wiele graczy w grze - 4 w jednej rozgrywce
        self._players.append(player)

    def is_ready(self):
        if len(self._players) == 4:
            return True
        else:
            pass
            # todo jakis error

    def prepare_players(self):
        decks = get_decks()
        for i in range(4):
            player = self._players[i]
            player.set_deck(decks[i])
            self._players[i] = player


    def game_start(self):
        if self.is_ready():
            self.prepare_players()

    def get_player_decks(self):
        for player in self._players:
            print(get_decks())

    def get_players(self):
        for player in self._players:
            print(player)