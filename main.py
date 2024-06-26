from gamemaster import GameMaster
from player import Player
gm = GameMaster()

p1 = Player("1", "B")
p2 = Player("2", "D")
p3 = Player("3", "F")
p4 = Player("4", "H")
gm.add_player(p1)
gm.add_player(p2)
gm.add_player(p3)
gm.add_player(p4)
gm.game_start()
