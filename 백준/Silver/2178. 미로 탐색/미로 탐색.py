import sys
from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def input():
    return sys.stdin.readline().rstrip()

def bfs(N, M, board, distances, visited):
    deq = deque([(0, 0)])
    visited[0][0] = True

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                deq.append((nx, ny))
                distances[nx][ny] += distances[x][y]

    return distances[N - 1][M - 1]


def solve(N, M, board):
    distances = [[1] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    return bfs(N, M, board, distances, visited)

def main():
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
    
    answer = solve(N, M, board)
    print(answer)

if __name__ == "__main__":
    main()