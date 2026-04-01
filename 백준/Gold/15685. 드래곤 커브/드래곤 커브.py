dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    dx, dy = dxy[d]
    x, y = x + dx, y + dy
    board[y][x] = 1

    if g > 0:
        d = (d + 1) % 4
        dx, dy = dxy[d]
        x, y = x + dx, y + dy
        board[y][x] = 1

    dir = [d]
    for _ in range(g - 1):
        temp = list(dir)
        dir.reverse()
        for idx in range(len(dir)):
            dir[idx] = (dir[idx] + 1) % 4
        dir += temp

        for i in dir:
            dx, dy = dxy[i]
            x, y = x + dx, y + dy
            board[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            cnt += 1

print(cnt)