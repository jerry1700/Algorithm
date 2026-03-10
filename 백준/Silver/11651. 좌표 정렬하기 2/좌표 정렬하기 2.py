N = int(input())

xy = [list(map(int, input().split())) for i in range(N)]
sort_xy = sorted(xy, key = lambda x: (x[1], x[0]))

for x, y in sort_xy:
    print(x, y)
