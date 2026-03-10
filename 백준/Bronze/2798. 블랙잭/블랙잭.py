N, M = map(int, input().split())
card = list(map(int, input().split()))

black = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            test_sum = card[i] + card[j] + card[k]
            if test_sum <= M:
                black.append(test_sum)

print(max(black))
