dxy = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

def solution(board):
    x = len(board)
    y = len(board[0])
    boom = [[0] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if board[i][j] == 1:
                boom[i][j] = 1
                for dx, dy in dxy:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < x and 0 <= ny < y:
                        boom[nx][ny] = 1

    answer = 0
    for i in range(x):
        for j in range(y):
            if boom[i][j] == 0:
                answer += 1
                
    return answer