N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 2

def whiteblue(start_x, start_y, N, papers):
    half = N // 2
    num = papers[start_x][start_y]
    test = True

    for i in range(N):
        for j in range(N):
            if papers[i + start_x][j + start_y] != num:
                test = False
                break
        
        if not test:
            break

    if test:
        if num == 0:
            cnt[0] += 1
            return
        elif num == 1:
            cnt[1] += 1
            return
    else:
        whiteblue(start_x, start_y, half, papers)
        whiteblue(start_x, start_y + half, half, papers)
        whiteblue(start_x + half, start_y, half, papers)
        whiteblue(start_x + half, start_y + half, half, papers)

whiteblue(0, 0, N, papers)
print(*cnt, sep = "\n")