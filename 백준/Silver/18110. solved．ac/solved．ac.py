import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    hard = [int(input()) for i in range(n)]
    hard.sort()
    scope = int(n * 15 / 100 + 0.5)
    hard_sum = 0

    for i in range(scope, n - scope):
        hard_sum += hard[i]

    print(int(hard_sum / (n - 2 * scope) + 0.5))
