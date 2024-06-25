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

    def set_deck(self, deck):
        self._deck = deck
    
