import copy
from collections import deque

dxyz = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
start = [0, 0, 0]
end = [4, 4, 4]

maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
restore = [[row[:] for row in layer] for layer in maze]

def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def backtracking1(depth):
    global maze
    global answer

    if depth == 5:
        for a, b, c, d, e in sequences:
            for idx, s in enumerate(sequence):
                for _ in range(s):
                    maze[idx] = rotate(maze[idx])

            if answer == 12:
                return
            
            maze[0], maze[1], maze[2], maze[3], maze[4] = maze[a], maze[b], maze[c], maze[d], maze[e]
            distance = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
            z, x, y = start[0], start[1], start[2]
            if maze[z][x][y] == 0:
                continue
            distance[z][x][y] = 0

            deq = deque([(z, x, y)])
            while deq:
                z, x, y = deq.popleft()
                if distance[z][x][y] >= answer:
                    break
                
                for dx, dy, dz in dxyz:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and maze[nz][nx][ny] == 1 and distance[nz][nx][ny] == -1:
                        distance[nz][nx][ny] = distance[z][x][y] + 1
                        deq.append((nz, nx, ny))

            if  0 <= distance[end[0]][end[1]][end[2]] < answer:
                answer = distance[end[0]][end[1]][end[2]]

            maze = [[row[:] for row in layer] for layer in restore]
        return
    
    for i in range(4):
        sequence.append(i)
        backtracking1(depth + 1)
        sequence.pop()

def backtracking2(depth):
    if depth == 5:
        sequences.append(sequence[:])
        return
    for i in range(5):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            backtracking2(depth + 1)
            sequence.pop()
            visited[i] = False

sequences = []
sequence = []
visited = [False] * 5
backtracking2(0)

sequence = []
answer = float('inf')
backtracking1(0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)