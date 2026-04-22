from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def escape(maze, fire, i, j):
    jihoon = [[-1] * C for _ in range(R)]

    deq = deque([(i, j)])
    jihoon[i][j] = 0

    while deq:
        x, y = deq.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C):
                return jihoon[x][y] + 1
            if 0 <= nx < R and 0 <= ny < C and jihoon[nx][ny] == -1 and maze[nx][ny] != "#" and (fire[nx][ny] == -1 or jihoon[x][y] + 1 < fire[nx][ny]):
                jihoon[nx][ny] = jihoon[x][y] + 1
                deq.append((nx, ny))
            
    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

fire_location = [(i, j) for i in range(R) for j in range(C) if maze[i][j] == "F"]
fire = [[-1] * C for _ in range(R)]

deq = deque(fire_location)
for i, j in fire_location:
    fire[i][j] = 0

while deq:
    x, y = deq.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and fire[nx][ny] == -1 and maze[nx][ny] != "#":
            fire[nx][ny] = fire[x][y] + 1
            deq.append((nx, ny))

for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            answer = escape(maze, fire, i, j)

print(answer)