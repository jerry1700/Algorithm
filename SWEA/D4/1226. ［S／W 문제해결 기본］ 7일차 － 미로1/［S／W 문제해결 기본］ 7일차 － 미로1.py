from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(sx, sy, ex, ey, board):
    deq = deque([(sx, sy)])
    visited = [[False] * 16 for _ in range(16)]
    visited[sx][sy] = True

    while deq:
        x, y = deq.popleft()

        if x == ex and y == ey:
            return 1
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx, ny))

    return 0

for _ in range(10):
    tc = int(input())
    board = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sx, sy = i, j
            elif board[i][j] == 3:
                ex, ey = i, j

    answer = bfs(sx, sy, ex, ey, board)

    if answer:
        print(f"#{tc} {answer}")
    else:
        print(f"#{tc} {answer}")