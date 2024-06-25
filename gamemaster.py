from player import Player

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
            # todo

    def game_start(self):
        pass