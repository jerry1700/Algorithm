import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def bfs(N, M, board):
    starts = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                starts.append((i, j))
    
    days = [[-1] * M for _ in range(N)]
    
    deq = deque(starts)
    for start in starts:
        days[start[0]][start[1]] = 0

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and days[nx][ny] == -1 and board[nx][ny] == 0:
                days[nx][ny] = days[x][y] + 1
                deq.append((nx, ny))

    return days

def solve(N, M, board):
    days = bfs(N, M, board)
    result = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and days[i][j] == -1:
                return -1
            
            if days[i][j] > result:
                result = days[i][j]

    return result

def main():
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = solve(N, M, board)
    print(answer)

if __name__ == "__main__":
    main()