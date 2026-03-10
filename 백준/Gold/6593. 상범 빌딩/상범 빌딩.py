from collections import deque

dxyz = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

def bfs(L, R, C, board1, visited, start, end):
    visited[start[0]][start[1]][start[2]] = 0
    deq = deque([start])

    while deq:
        z, y, x = deq.popleft()
        for dx, dy, dz in dxyz:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (end[0], end[1], end[2]) == (nz, ny, nx):
                return visited[z][y][x] + 1
            
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L and visited[nz][ny][nx] == -1 and board1[nz][ny][nx] == ".":
                visited[nz][ny][nx] = visited[z][y][x] + 1
                deq.append((nz, ny, nx))

    return "Trapped!"

while True:
    L, R, C = map(int, input().split())

    if (L, R, C) == (0, 0, 0):
        break

    board1 = []
    for _ in range(L):
        board2 = []
        for _ in range(R):
            board2.append(list(input()))
        temp = input()
        board1.append(board2)

    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board1[i][j][k] == "S":
                    start = (i, j, k)
                if board1[i][j][k] == "E":
                    end = (i, j, k)

    answer = bfs(L, R, C, board1, visited, start, end)
    
    if type(answer) == int:
        print(f"Escaped in {answer} minute(s).")
    else:
        print(answer)