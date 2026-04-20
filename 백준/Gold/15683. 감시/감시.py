N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]

dirs = [
    [],
    [[(1, 0)], [(0, 1)], [(-1, 0)], [(0, -1)]],
    [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
    [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)]],
    [[(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]],
    [[(1, 0), (0, 1), (-1, 0), (0, -1)]]
]
dir = [0, 4, 2, 4, 4, 1]

cctv_position = []
cctv_num = []
for i in range(N):
    for j in range(M):
        if 1 <= temp[i][j] <= 5:
            cctv_position.append((i, j))
            cctv_num.append(temp[i][j])

def backtracking(depth):
    if depth == len(cctv_num):
        sequences.append(sequence[:])
        return
    
    c = cctv_num[depth]
    for i in range(dir[c]):
        sequence.append(i)
        backtracking(depth + 1)
        sequence.pop()

sequences = []
sequence = []
backtracking(0)

answer = float("inf")
for seq in sequences:
    board = [row[:] for row in temp]

    for i in range(len(cctv_position)):
        x, y = cctv_position[i]
        c = cctv_num[i]
        idx = seq[i]

        for dx, dy in dirs[c][idx]:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < N and 0 <= ny < M) or board[nx][ny] == 6:
                    break
                if board[nx][ny] == 0:
                    board[nx][ny] = 10
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    if cnt < answer:
        answer = cnt

print(answer)