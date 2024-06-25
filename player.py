from game import Deck

class Player:
    def __init__(self, deck, name, lastname, partner = None, turn = False, is_dummy = False):
        self._deck = deck
        self._name = name
        self._lastname = lastname
        self._partner = partner
        self._turn = turn
        self._is_dummy = is_dummy

    # todo Partner

    def get_name(self):
        return self._name

    def get_lastname(self):
        return self._lastname

    def get_fullname(self):
        return self.get_name() + self.get_lastname

    def get_turn(self):
        return self._turn

    def get_is_dummy(self):
        return self._is_dummy

    def set_turn(self, turn):
        if(self.verify_bool(turn)):
            self._turn = turn
        else:
            raise ValueError("turn has to be boolean\n")

    def set_is_dummy(self, is_dummy):
        if(self.verify_bool(is_dummy)):
            self._is_dummy = is_dummy
        else:
            raise ValueError("is_dummy has to be boolean\n")

    def verify_bool(value):
        if value == True or value == False:
            return True
        else:
            return False