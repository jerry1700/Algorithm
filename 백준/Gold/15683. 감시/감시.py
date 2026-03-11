from itertools import product

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
step = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]],
}

cctv_count = 0
cctv_list = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv_list.append([office[i][j], i, j])
            cctv_count += 1

pick = [step[t] for t, x, y in cctv_list]
blind_spot = N * M
for case in product(*pick):
    test = [row[:] for row in office]
    cnt = 0
    
    for idx, dir in enumerate(case):
        c, i, j = cctv_list[idx]
        for s in dir:
            dx, dy = dxy[s]
            nx, ny = i + dx, j + dy
            while 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
                test[nx][ny] = "#"
                nx += dx
                ny += dy

    cnt = sum(r.count(0) for r in test)
    
    if cnt < blind_spot:
        blind_spot = cnt

print(blind_spot)