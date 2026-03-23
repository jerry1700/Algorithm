N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

shape = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 1), (1, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
]

def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

def flip(board):
    return [row[::-1] for row in board]

def cal_total(board, s):
    N = len(board)
    M = len(board[0])
    max_total = 0

    for i in range(N):
        for j in range(M):
            total = 0
            for dx, dy in shape[s]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    total += board[nx][ny]
            
            if total > max_total:
                max_total = total
    
    return max_total

group = []
for _ in range(4):
    for i in range(5):
        group.append(cal_total(board, i))
    board = rotate(board)
board = flip(board)
for _ in range(4):
    for i in range(5):
        group.append(cal_total(board, i))
    board = rotate(board)

print(max(group))