import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def bfs(n, m, board, visited, start):
    draw = 1
    deq = deque([start])
    visited[start[0]][start[1]] = True

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                deq.append((nx, ny))
                draw += 1

    return draw

def solve(n, m, board):
    draws = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                draw = bfs(n, m, board, visited, start = (i, j))
                draws.append(draw)

    return len(draws), max(draws) if draws else 0

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    answer = solve(n, m, board)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()