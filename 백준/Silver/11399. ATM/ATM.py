N = int(input())
P = list(map(int, input().split()))
P.sort()
time = sorted(P)

for i in range(1, N):
    time[i] = sum(P[:i + 1])

print(sum(time))
