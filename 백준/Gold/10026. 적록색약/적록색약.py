from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
board = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == "R" and not visited[i][j]:
            deq = deque([(i, j)])
            visited[i][j] = True
            while deq:
                x, y = deq.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == "R":
                        visited[nx][ny] = True
                        deq.append((nx, ny))
            
            cnt += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == "G" and not visited[i][j]:
            deq = deque([(i, j)])
            visited[i][j] = True
            while deq:
                x, y = deq.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == "G":
                        visited[nx][ny] = True
                        deq.append((nx, ny))
            
            cnt += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == "B" and not visited[i][j]:
            deq = deque([(i, j)])
            visited[i][j] = True
            while deq:
                x, y = deq.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == "B":
                        visited[nx][ny] = True
                        deq.append((nx, ny))
            
            cnt += 1

visited = [[False] * N for _ in range(N)]
cnt2 = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == "B" and not visited[i][j]:
            deq = deque([(i, j)])
            visited[i][j] = True
            while deq:
                x, y = deq.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == "B":
                        visited[nx][ny] = True
                        deq.append((nx, ny))
            
            cnt2 += 1

for i in range(N):
    for j in range(N):
        if board[i][j] != "B" and not visited[i][j]:
            deq = deque([(i, j)])
            visited[i][j] = True
            while deq:
                x, y = deq.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] != "B":
                        visited[nx][ny] = True
                        deq.append((nx, ny))
            
            cnt2 += 1

print(cnt, cnt2)