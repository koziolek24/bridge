from decks import get_decks, get_bid, get_bid_info, get_end


class GameMaster:
    def __init__(self):
        self._players = []
        self._contract = None
        self._side = None
        self._declarer = None
        self._dummy = None
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
            self.prepare()
            self.gameplay()

    def get_players(self):
        for player in self._players:
            print(player)

    def bidding(self):
        bids = []
        while True:
            for i in range(4):
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
                        self._players[(player_id + 1) % 4].set_turn(True)
                        # we set turn to player next to declarer
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
        # first we find player whose turn it is
        index = 0
        for i in range(4):
            if self._players[i].get_turn() is True:
                index = i
                break
        lead = False
        while True:
            if self._players[index].is_empty_deck() is True:
                break
            for i in range(4):
                if self._players[index+i].is_empty_deck() is True:
                    break
                if lead is False:
                    self._players[index+i].play_lead()
                    lead = True
                elif self._players[index+i].get_is_dummy() is True:
                    self._declarer.dummy_play()
                    pass
                else:
                    self._players[index+i].get_play(self._dummy)

    def display(self):
        # todo display
        pass

    def prepare(self):
        self._players[0].set_partner(self._players[2])
        self._players[1].set_partner(self._players[3])
        self._players[2].set_partner(self._players[0])
        self._players[3].set_partner(self._players[1])

        self._dummy = self._declarer.get_partner()
        self._dummy.set_is_dummy(True)
        # we set partners to each player, and we set declarer partner to dummy
