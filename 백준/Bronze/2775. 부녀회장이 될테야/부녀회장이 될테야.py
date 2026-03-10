T = int(input())

for test in range(T):
    k = int(input())
    n = int(input())

    citizen = [[0] * (n + 1) for i in range(k + 1)]

    for i in range(n + 1):
        citizen[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            citizen[i][j] = citizen[i - 1][j] + citizen[i][j - 1]

    print(citizen[k][n])
