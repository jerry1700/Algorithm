from collections import deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())
op = [list(input().split()) for _ in range(L)]
for i in range(L - 2, -1, -1):
    op[i + 1][0] = int(op[i + 1][0]) - int(op[i][0])
    
d = 0
time = 1
out = False
body = deque([(0, 0)])

for X, C in op:
    X = int(X)
    dx, dy = dxy[d]
    for _ in range(X):
        x, y = body[-1]
        nx, ny = x + dx, y + dy
        if (not (0 <= nx < N and 0 <= ny < N)) or (nx, ny) in body:
            out = True
            break
            
        if board[nx][ny] == 1:
            body.append((nx, ny))
            board[nx][ny] = 0
        else:
            body.popleft()
            body.append((nx, ny))
        time += 1
        
    if out:
        print(time)
        break
        
    if C == "L":
        d = (d - 1) % 4
    elif C == "D":
        d = (d + 1) % 4

while not out:
    x, y = body[-1]
    dx, dy = dxy[d]
    nx, ny = x + dx, y + dy
    if (not (0 <= nx < N and 0 <= ny < N)) or (nx, ny) in body:
        out = True
        print(time)
        break
        
    if board[nx][ny] == 1:
        body.append((nx, ny))
        board[nx][ny] = 0
    else:
        body.popleft()
        body.append((nx, ny))
    time += 1