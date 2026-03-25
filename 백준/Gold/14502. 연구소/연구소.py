from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [list(row) for row in board]

candi = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 0]

def backtracking(start, depth):
    global board
    global max_cnt

    if depth == 3:
        for i in sequence:
            x, y = candi[i]
            board[x][y] = 1
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == 2:
                    deq = deque([(i, j)])

                    while deq:
                        x, y = deq.popleft()
                        for dx, dy in dxy:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                                board[nx][ny] = 2
                                deq.append((nx, ny))
        
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

        board = [list(row) for row in temp]

        return
    
    for i in range(start, len(candi)):
        sequence.append(i)
        backtracking(i + 1, depth + 1)
        sequence.pop()

sequence = []
max_cnt = 0
backtracking(0, 0)

print(max_cnt)