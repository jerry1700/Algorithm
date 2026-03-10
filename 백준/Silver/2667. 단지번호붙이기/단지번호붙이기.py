from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(N, board, visited, start):
    large = 0
    visited[start[0]][start[1]] = True
    deq = deque([start])

    while deq:
        x, y = deq.popleft()
        large += 1
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                deq.append((nx, ny))

    return large

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

cnt = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            cnt.append(bfs(N, board, visited, start = (i, j)))

print(len(cnt))
print(*sorted(cnt), sep = "\n")