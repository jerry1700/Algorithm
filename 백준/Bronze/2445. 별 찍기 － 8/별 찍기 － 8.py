N = int(input())

for i in range(1, 2 * N):
    print(f'{" " * 2 * abs(N - i):*^{2 * N}}')
