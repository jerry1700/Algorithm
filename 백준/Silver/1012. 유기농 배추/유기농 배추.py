from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())

def bfs(N, M, board, visited, start):
    deq = deque([start])
    visited[start[0]][start[1]] = True

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                deq.append((nx, ny))
    
    return 1

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1

    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                answer = bfs(N, M, board, visited, start = (i, j))
                cnt += 1
    
    print(cnt)