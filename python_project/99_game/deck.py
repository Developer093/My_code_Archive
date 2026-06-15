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

    def deal_cards(self, player_count, card_count):
        hands = []

        # 플레이어 수만큼 빈 손패 생성
        for _ in range(player_count):
            hands.append([])

        # 카드 분배
        for _ in range(card_count):
            for hand in hands:
                hand.append(self.draw_card())

        return hands