class card:
    def __init__(self, color, value):
        self._color = color
        self._value = value

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def get_card(self):
        return self.get_value() + self.get_color()

