N = int(input())

xy = [list(map(int, input().split())) for i in range(N)]
sort_xy = sorted(xy)

for x, y in sort_xy:
    print(x, y)
