from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                sx, sy = i, j
            elif board[i][j] == 3:
                ex, ey = i, j

    dis = [[-1] * N for _ in range(N)]
    deq = deque([(sx, sy)])
    dis[sx][sy] = 0

    answer = 0

    while deq:
        x, y = deq.popleft()

        if (x, y) == (ex, ey):
            answer = dis[x][y] - 1
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                deq.append((nx, ny))

    print(f"#{tc} {answer}")