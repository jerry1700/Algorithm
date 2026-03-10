import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def bfs(M, N, board, visited, start):
    large = 1

    deq = deque([start])
    visited[start[0]][start[1]] = True
    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                large += 1
                deq.append((nx, ny))

    return large

M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            board[y][x] = 1

visited = [[False] * N for _ in range(M)]

cnt = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and not visited[i][j]:
            answer = bfs(M, N, board, visited, start = (i, j))
            cnt.append(answer)

print(len(cnt))
print(*sorted(cnt))