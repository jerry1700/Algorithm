from collections import deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == "X":
                sx, sy = i, j
            elif board[i][j] == "Y":
                ex, ey = i, j

    visited = [[[[float("inf")] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    deq = deque([(sx, sy, 0, 0, 0)])
    visited[sx][sy][0][0] = 0

    answer = float("inf")

    while deq:
        x, y, d, k, count = deq.popleft()

        if count > visited[x][y][d][k]:
            continue

        if (x, y) == (ex, ey):
            answer = min(answer, count)
            continue

        for nd in range(4):
            diff = abs(nd - d)
            cnt = diff if diff <= 2 else 4 - diff

            nx, ny = x + dxy[nd][0], y + dxy[nd][1]
            if 0 <= nx < N and 0 <= ny < N:
                new_count = count + cnt + 1

                if board[nx][ny] != "T":
                    if visited[nx][ny][nd][k] > new_count:
                        visited[nx][ny][nd][k] = new_count
                        deq.append((nx, ny, nd, k, new_count))
                elif k < K:
                    if visited[nx][ny][nd][k + 1] > new_count:
                        visited[nx][ny][nd][k + 1] = new_count
                        deq.append((nx, ny, nd, k + 1, new_count))

    print(f"#{tc} {answer if answer != float('inf') else -1}")