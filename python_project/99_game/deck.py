import random

class Deck:
    def __init__(self):
        self.cards = []

        suits = ["♠", "♥", "♦", "♣"]

        for suit in suits:
            for number in range(1, 14):
                self.cards.append((suit, number))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()