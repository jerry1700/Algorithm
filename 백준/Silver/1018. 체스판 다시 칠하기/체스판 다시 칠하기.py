N, M = map(int, input().split())
chess = [list(input()) for i in range(N)]
right_chess1 = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]
right_chess2 = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]

draw_min = N * M
for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0
        for x in range(8):
            for y in range(8):
                if chess[x + i][y + j] != right_chess1[x][y]:
                    cnt1 += 1
                if chess[x + i][y + j] != right_chess2[x][y]:
                    cnt2 += 1

        if min(cnt1, cnt2) < draw_min:
            draw_min = min(cnt1, cnt2)

print(draw_min)
