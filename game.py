class card:
    def __init__(self, value, color):
        self._value = value
        self._color = color

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def get_card(self):
        return str(self.get_value()) + self.get_color()


class deck:
    def __init__(self, deck = []):
        self.deck = deck

    def get_deck(self):
        for card in self.deck:
            print(card.get_card(), end="")
