from collections import deque
from itertools import combinations

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [list(row) for row in board]

virus = []
candi = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            candi.append((i, j))

max_cnt = 0
for i in combinations(range(len(candi)), 3):
    for idx in i:
        x, y = candi[idx]
        board[x][y] = 1

    deq = deque(virus)

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                deq.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

    board = [list(row) for row in temp]

print(max_cnt)