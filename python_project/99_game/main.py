
# 구십구 99 프로젝트
# Day 1 - 카드 덱 생성
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

random.shuffle(deck)
# 결과 출력
print("카드 덱")
print(deck)

print()

print("총 카드 수 :", len(deck))

