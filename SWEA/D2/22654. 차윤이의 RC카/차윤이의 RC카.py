T = int(input())

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == "X":
                tx, ty = i, j
                break

    Q = int(input())
    result = []

    for _ in range(Q):
        C, ops = list(input().split())

        x, y = tx, ty
        d = 0
        dx, dy = dxy[d]

        for op in ops:
            if op == "A":
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != "T":
                    x, y = nx, ny
            elif op == "L":
                d = (d - 1) % 4
                dx, dy = dxy[d]
            elif op == "R":
                d = (d + 1) % 4
                dx, dy = dxy[d]

        if board[x][y] == "Y":
            result.append(1)
        else:
            result.append(0)

    print(f"#{tc}", *result)