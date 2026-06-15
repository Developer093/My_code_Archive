
# 구십구 99 프로젝트
# Day 1 - 카드 덱 생성 + 카드 섞기 + 패 분배

import random

deck = []

# 일반 카드 1~8 (각 3장)
for card in range(1, 9):
    for _ in range(3):
        deck.append(card)

# 일반 카드 10 (10장)
for _ in range(10):
    deck.append(10)

# 특수 카드 ±9 (5장)
for _ in range(5):
    deck.append("±9")

# 특수 카드 ±10 (6장)
for _ in range(6):
    deck.append("±10")

# 특수 카드 0 (3장)
for _ in range(3):
    deck.append("0")

# 특수 카드 J (1장)
deck.append("J")

# 카드 섞기
random.shuffle(deck)

# 플레이어와 컴퓨터의 패
player_hand = []
computer_hand = []

# 5장씩 분배
for _ in range(5):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())

# 결과 출력
print("플레이어 패")
print(player_hand)

print()

print("컴퓨터 패")
print(computer_hand)

print()

print("남은 카드 덱")
print(deck)

print()

print("남은 카드 수 :", len(deck))
