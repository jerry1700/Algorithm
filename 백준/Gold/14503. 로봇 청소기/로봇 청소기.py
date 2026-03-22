import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

move = [(r, c)]
cnt = 0

while move:
    x, y = move.pop()
    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1

    clean = False
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            clean = True

    if clean:
        while True:
            d = (d - 1) % 4
            dx, dy = dxy[d]
            nx, ny = x + dx, y + dy
            if board[nx][ny] == 0:
                move.append((nx, ny))
                break
    else:
        dx, dy = dxy[d]
        nx, ny = x - dx, y - dy
        if board[nx][ny] == 1:
            break
        else:
            move.append((nx, ny))

print(cnt)