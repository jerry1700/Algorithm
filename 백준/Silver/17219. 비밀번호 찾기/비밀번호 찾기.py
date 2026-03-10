N, M = map(int, input().split())
password = password = {i: j for _ in range(N) for i, j in [input().split()]}
site = [input() for i in range(M)]

for i in site:
    print(password.get(i))
