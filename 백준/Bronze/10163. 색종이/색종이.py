n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

pmap = [[0] * 1001 for _ in range(1001)]
start = 1
for x1, y1, dx, dy in paper:
    for y in range(y1, y1 + dy):
            pmap[y][x1:x1 + dx] = [start] * dx
    start += 1

for s in range(1, start - 1):
    cnt = 0
    for i in range(1001):
        cnt += pmap[i].count(s)
    print(cnt)
print(dx * dy)
