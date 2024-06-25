from decks import get_decks, get_bid


class GameMaster:
    def __init__(self):
        self._players = []
        self._contract = None
        self._side = None
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
            # todo sorting of cards

    def game_start(self):
        if self.is_ready():
            self.prepare_players()
            self.bidding()

    def get_players(self):
        for player in self._players:
            print(player)

    def check_end(self, bids):
        size = len(bids)
        if bids[size - 1] == "pass" and bids[size - 2] == "pass" and bids[size - 3] == "pass" and bids[size - 4] == "pass":
            return True

    def bidding(self):
        bids = []
        while True:
            # player bids
            # verification of bid
            # 4 passes -> stop
            for player in self._players:
                print(bids[-4:])
                bids = get_bid(bids)
                if len(bids) > 3 and self.check_end(bids):
                    self._contract = bids[-5]
                    # todo special case when counter or re-counter
                    # todo get sides
                    return
