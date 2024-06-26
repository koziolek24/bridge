class Card:
    def __init__(self, value, color):
        self._value = value
        self._color = color

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def get_card(self):
        return str(self.get_value()) + self.get_color()


class Deck:
    def __init__(self, deck=[]):
        self._deck = deck

    def get_deck(self):
        deck_values = ""
        for card in self._deck:
            deck_values += card.get_card()
            deck_values += " "
        return deck_values

    def remove_card(self, card):
        for cards in self._deck:
            if cards.get_card() == card.get_card():
                self._deck.remove(cards)
                return
        raise ValueError("Card not removed")

    def set_deck(self, deck):
        self._deck = deck
    
    def is_empty(self):
        if len(self._deck) == 0:
            return True
        return False

    def is_in_deck(self, card):
        for deck_card in self._deck:
            if deck_card.get_card() == card.get_card():
                return True
        return False

    def is_color_in_deck(self, color):
        for deck_card in self._deck:
            if deck_card.get_color() == color:
                return True
        return False
