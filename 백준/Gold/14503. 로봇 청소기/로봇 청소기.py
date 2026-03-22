from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
wall = [list(row) for row in board]

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

deq = deque([(r, c)])

cnt = 0
while deq:
    x, y = deq.popleft()
    if board[x][y] == 0:
        board[x][y] = 1
        cnt += 1
    clean = False
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            clean = True

    if clean:
        while True:
            d -= 1
            if not (0 <= d < 4):
                d = (d + 4) % 4
            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy
            if board[nx][ny] == 0:
                deq.append((nx, ny))
                break
    else:
        dx, dy = dxy[d]
        nx, ny = x - dx, y - dy
        if wall[nx][ny] == 1:
            break
        else:
            deq.append((nx, ny))

print(cnt)