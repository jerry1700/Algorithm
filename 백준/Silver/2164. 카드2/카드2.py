from collections import deque

N = int(input())
card = deque(range(1, N + 1))

while len(card) > 1:
    card.popleft()
    if card:
        card.rotate(-1)

print(card[0])
