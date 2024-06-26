from gamemaster import GameMaster
from player import Player
gm = GameMaster()

p1 = Player("A", "B")
p2 = Player("C", "D")
p3 = Player("E", "F")
p4 = Player("G", "H")
gm.add_player(p1)
gm.add_player(p2)
gm.add_player(p3)
gm.add_player(p4)
gm.game_start()
