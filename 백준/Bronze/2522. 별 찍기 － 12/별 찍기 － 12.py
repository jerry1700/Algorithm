N = int(input())

for i in range(1, 2 * N):
    print(f'{" " * abs(N - i):*<{N}}')
