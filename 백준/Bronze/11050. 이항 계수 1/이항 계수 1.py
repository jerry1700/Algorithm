N, K = map(int, input().split())

Nfact = 1
for i in range(K):
    Nfact *= (N - i)

Kfact = 1
for i in range(1, K + 1):
    Kfact *= i

print(Nfact // Kfact)
