from decks import get_decks, get_bid, get_bid_info, get_end


class GameMaster:
    def __init__(self):
        self._players = []
        self._contract = None
        self._side = None
        self._declarer = None
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
            print("Not enough players in this game")
            return False

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
            self.gameplay()

    def get_players(self):
        for player in self._players:
            print(player)

    def bidding(self):
        bids = []
        while True:
            for player in self._players:
                print(bids[-4:])
                bids = get_bid(bids)
                if get_end(bids):
                    contract, player_id = get_bid_info(bids)
                    if player_id == -1:
                        self._contract = None
                        self._side = None
                        self._declarer = None
                        print("There is no contract - 4 passes")
                    else:
                        self._declarer = self._players[player_id]
                        self._side = self._declarer.get_side()
                        self._contract = contract
                        print(self._contract)
                        print(self._declarer.get_fullname())
                    return

    def gameplay(self):
        # we have contract
        # we know which side has contract
        # we know who is going to be a dummy
        # 3 types of turns:
        # 1 one starting and revealing dummy
        # 2 normal
        # 3 dummy
        self.display()
        pass

    def display(self):
        # todo display
        pass

