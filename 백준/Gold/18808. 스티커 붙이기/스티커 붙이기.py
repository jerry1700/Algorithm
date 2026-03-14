N, M, K = map(int, input().split())
notebook = [[0] * M for _ in range(N)]

def check(i, j, R, C):
    for dx in range(R):
        for dy in range(C):
            if i + dx >= N or j + dy >= M:
                return False
            if sticker[dx][dy] == 1:
                if notebook[i + dx][j + dy] == 1:
                    return False
    return True

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [tuple(map(int, input().split())) for _ in range(R)]
    rot = 0

    test = False
    while not test:
        test = False
        R = len(sticker)
        C = len(sticker[0])

        for i in range(N):
            for j in range(M):
                test = check(i, j, R, C)
                if test:
                    break
            if test:
                break

        if test:
            for dx in range(R):
                for dy in range(C):
                    if sticker[dx][dy] == 1:
                        notebook[i + dx][j + dy] = 1
        else:
            sticker = list(zip(*sticker[::-1]))
            rot += 1
            if rot > 3:
                break
    
cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            cnt += 1

print(cnt)