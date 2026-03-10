from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(N, board, height, start):
    cnt = 0
    deq = deque([start])
    visited[start[0]][start[1]] = True

    while deq:
        x, y = deq.popleft()
        cnt += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] > height:
                visited[nx][ny] = True
                deq.append((nx, ny))
        
    return cnt

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for i in range(N):
    for j in range(N):
        if board[i][j] > max_height:
            max_height = board[i][j]

safe = []
for height in range(1, max_height + 1):
    cnt = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > height and not visited[i][j]:
                cnt.append(bfs(N, board, height, start = (i, j)))

    safe.append(cnt)

for i in range(len(safe)):
    safe[i] = len(safe[i])

if max(safe) == 0:
    print(1)
else:
    print(max(safe))