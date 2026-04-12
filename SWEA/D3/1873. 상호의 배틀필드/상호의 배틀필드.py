dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    ops = list(input())

    for i in range(H):
        for j in range(W):
            if board[i][j] == "^":
                x, y = i, j
                dx, dy = dxy[0]
                board[i][j] = "."
                break
            elif board[i][j] == "v":
                x, y = i, j
                dx, dy = dxy[1]
                board[i][j] = "."
                break
            elif board[i][j] == "<":
                x, y = i, j
                dx, dy = dxy[2]
                board[i][j] = "."
                break
            elif board[i][j] == ">":
                x, y = i, j
                dx, dy = dxy[3]
                board[i][j] = "."
                break

    for op in ops:
        if op == "U":
            dx, dy = dxy[0]
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
                x, y = nx, ny
        elif op == "D":
            dx, dy = dxy[1]
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
                x, y = nx, ny
        elif op == "L":
            dx, dy = dxy[2]
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
                x, y = nx, ny
        elif op == "R":
            dx, dy = dxy[3]
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
                x, y = nx, ny
        elif op == "S":
            nx, ny = x + dx, y + dy
            while 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == "#":
                    break
                if board[nx][ny] == "*":
                    board[nx][ny] = "."
                    break

                nx, ny = nx + dx, ny + dy

    if (dx, dy) == dxy[0]:
        board[x][y] = "^"
    elif (dx, dy) == dxy[1]:
        board[x][y] = "v"
    elif (dx, dy) == dxy[2]:
        board[x][y] = "<"
    elif (dx, dy) == dxy[3]:
        board[x][y] = ">"

    print(f"#{tc}", end = " ")
    for b in board:
        print("".join(b))