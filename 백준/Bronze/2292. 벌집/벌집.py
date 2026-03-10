N = int(input())
n = 1

while n * (n - 1) * 3 + 1 < N:
    n += 1

print(n)
