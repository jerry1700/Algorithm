N = int(input())

Nfact = 1
for i in range(1, N + 1):
    Nfact *= i

cnt = 0
while Nfact % 10 == 0:
    Nfact //= 10
    cnt += 1

print(cnt)
