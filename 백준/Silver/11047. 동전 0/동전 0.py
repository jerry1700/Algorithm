N, K = map(int, input().split())
money = [int(input()) for i in range(N)]

cnt = 0

for i in range(N - 1, -1, -1):
    if K == 0:
        break

    if money[i] <= K:
        cnt += (K // money[i])
        K %= money[i]

print(cnt)
