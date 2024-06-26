from decks import get_decks, get_bid, get_bid_info, get_end, get_winner


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
            if self._contract is not None:
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
                        if self._declarer.get_side() == 'N' or self._declarer.get_side() == 'S':
                            self._side = 'NS'
                        else:
                            self._side = 'EW'
                        self._contract = contract
                        self._players[(player_id + 1) % 4].set_turn(True)
                        # we set turn to player next to declarer
                        # print(self._contract)
                        # print(self._declarer.get_fullname())
                    return

    def gameplay(self):
        trump = self._contract[-1]
        index = 0
        for i in range(4):
            if self._players[i].get_turn() is True:
                index = i
                break
        lead = False
        score_ns = 0
        score_ew = 0
        for j in range(13):
            color = None
            if self._players[index].is_empty_deck() is True:
                break
            set_cards = []
            for i in range(4):
                idi = (index + i) % 4
                print()
                print(self._players[idi].get_fullname())
                print("NS: ", end="")
                print(score_ns, end=" ")
                print("EW: ", end="")
                print(score_ew)
                print()
                if i > 0:
                    color = set_cards[0][-1].get_color()
                if self._players[idi].is_empty_deck() is True:
                    break
                if lead is False:
                    set_cards.append((idi, self._players[idi].play_lead()))
                    lead = True
                elif self._players[idi].get_is_dummy() is True:
                    set_cards.append((idi, self._declarer.dummy_play(color)))
                    pass
                else:
                    set_cards.append((idi, self._players[idi].get_play(self._dummy, color)))
            index = get_winner(set_cards, trump)
            if self._players[index].get_side() == 'N' or self._players[index].get_side() == 'S':
                score_ns += 1
            else:
                score_ew += 1
        # checking of score
        if self._side == 'NS':
            score_ns = score_ns - 6 - int(self._contract[0])
            if score_ns < 0:
                print("You lost")
            else:
                print("You won")
        else:
            score_ew = score_ew - 6 - int(self._contract[0])
            if score_ew < 0:
                print("You lost")
            else:
                print("You won")

    def display(self):
        # todo display
        pass

    def prepare(self):
        self._players[0].set_partner(self._players[2])
        self._players[1].set_partner(self._players[3])
        self._players[2].set_partner(self._players[0])
        self._players[3].set_partner(self._players[1])
        self._players[0].set_side('N')
        self._players[1].set_side('E')
        self._players[2].set_side('S')
        self._players[3].set_side('W')
        self._dummy = self._declarer.get_partner()
        self._dummy.set_is_dummy(True)
        # we set partners to each player, and we set declarer partner to dummy
