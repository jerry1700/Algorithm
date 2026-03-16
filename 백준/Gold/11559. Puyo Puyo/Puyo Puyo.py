import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

board = [list(input()) for _ in range(12)]

answer = 0

while True:
    boom = False
    visited = [[False] * 6 for _ in range(12)]
    
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != ".":
                visited[i][j] = True
                deq = deque([(i, j)])
                cnt = 1
                test = [(i, j)]

                while deq:
                    x, y = deq.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == board[i][j]:
                            visited[nx][ny] = True
                            deq.append((nx, ny))
                            cnt += 1
                            test.append((nx, ny))

                if cnt >= 4:
                    boom = True
                    for x, y in test:
                        board[x][y] = "."

    if not boom:
        break

    answer += 1

    board = [list(row) for row in zip(*board[::-1])]
    for row in range(6):
        temp = []
        for r in board[row]:
            if r != ".":
                temp.append(r)
        temp += ["."] * (12 - len(temp))
        board[row] = temp
    board = [list(row) for row in zip(*board)][::-1]

print(answer)