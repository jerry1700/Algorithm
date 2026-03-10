N = int(input())
kgcm = [list(map(int, input().split())) for i in range(N)]

for kg, cm in kgcm:
    rank = 1
    for x, y in kgcm:
        if kg < x and cm < y:
            rank += 1

    print(rank, end = " ")
