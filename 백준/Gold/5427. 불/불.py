import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def escape_bfs(h, w, buildings, fires, escape, start):
    deq = deque([start])
    escape[start[0]][start[1]] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                return escape[x][y] + 1
            if escape[nx][ny] >= 0 or buildings[nx][ny] == "#":
                continue
            if escape[x][y] + 1 >= fires[nx][ny] and fires[nx][ny] != -1:
                continue
            escape[nx][ny] = escape[x][y] + 1
            deq.append((nx, ny))

    return "IMPOSSIBLE"

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    buildings = [list(input()) for _ in range(h)]
    fires = [[-1] * w for _ in range(h)]
    escape = [[-1] * w for _ in range(h)]

    fire = []
    for i in range(h):
        for j in range(w):
            if buildings[i][j] == "*":
                fire.append((i, j))

    for i, j in fire:
        fires[i][j] = 0
    deq = deque(fire)
    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and fires[nx][ny] == -1 and buildings[nx][ny] != "#":
                fires[nx][ny] = fires[x][y] + 1
                deq.append((nx, ny))
        
    for i in range(h):
        for j in range(w):
            if buildings[i][j] == "@":
                answer = escape_bfs(h, w, buildings, fires, escape, start = (i, j))
                print(answer)