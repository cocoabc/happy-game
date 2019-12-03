from collections import namedtuple


class Card(namedtuple('CardData', ['suit', 'value'])):
    suits = '♣ ♢ ♡ ♠'.split()


    def __new__(cls, suit, value):
        assert suit in cls.suits
        assert value in cls.values
        return super().__new__(cls, suit, value)

    def __str__(self):
        return '{} {}'.format(self.suit, self.value)


def generate_deck():
    """Generate sorted full deck of cards"""
    return [Card(suit, value)
            for suit in Card.suits for value in Card.values]
