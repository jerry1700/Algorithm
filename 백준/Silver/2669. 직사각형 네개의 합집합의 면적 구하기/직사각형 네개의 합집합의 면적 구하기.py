square = [list(map(int, input().split())) for _ in range(4)]
smap = [[0] * 100 for _ in range(100)]

for x1, y1, x2, y2 in square:
    for x in range(x1, x2):
        for y in range(y1, y2):
            smap[y][x] = 1


cnt = 0

for i in range(100):
    for j in range(100):
        if smap[i][j] == 1:
            cnt += 1

print(cnt)
