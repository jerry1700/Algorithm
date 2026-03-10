import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

jstart = []
fstart = []
for i in range(R):
    for j in range(C):
        if board[i][j] == "J":
            jstart.append((i, j))
        if board[i][j] == "F":
            fstart.append((i, j))

fdeq = deque(fstart)
fires = [[-1] * C for _ in range(R)]
for x, y in fstart:
    fires[x][y] = 0

while fdeq:
    x, y = fdeq.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and fires[nx][ny] == -1 and board[nx][ny] == ".":
            fires[nx][ny] = fires[x][y] + 1
            fdeq.append((nx, ny))

jdeq = deque(jstart)
jihoons = [[-1] * C for _ in range(R)]
for x, y in jstart:
    jihoons[x][y] = 0

def bfs(R, C, fires, jihoons, jdeq):
    while jdeq:
        x, y = jdeq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return jihoons[x][y] + 1
            if jihoons[nx][ny] >= 0 or board[nx][ny] == "#":
                continue
            if fires[nx][ny] != -1 and fires[nx][ny] <= jihoons[x][y] + 1:
                continue
            jihoons[nx][ny] = jihoons[x][y] + 1
            jdeq.append((nx, ny))
    return "IMPOSSIBLE"

answer = bfs(R, C, fires, jihoons, jdeq)
print(answer)