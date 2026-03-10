import sys
from collections import deque

knight = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    distances = [[-1] * l for _ in range(l)]

    deq = deque([start])
    distances[start[0]][start[1]] = 0
    while deq:
        x, y = deq.popleft()
        if x == end[0] and y == end[1]:
            print(distances[x][y])
            break
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                deq.append((nx, ny))