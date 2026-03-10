N = int(input())
card = list(map(int, input().split()))
M = int(input())
answer = list(map(int, input().split()))

card_map = [0] * 20000001
for i in card:
    card_map[i] += 1

for i in answer:
    print(card_map[i], end = " ")
