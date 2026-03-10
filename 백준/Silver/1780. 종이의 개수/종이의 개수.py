N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 3

def paper_cnt(start1, end1, start2, end2):
    num = papers[start1][start2]
    test = True
    
    for i in range(start1, end1):
        for j in range(start2, end2):
            if papers[i][j] != num:
                test = False
                break

        if not test:
            break

    if test:
        cnt[num + 1] += 1
        return
    
    ran = (end1 - start1) // 3

    for i in range(3):
        for j in range(3):
            next_start1 = start1 + i * ran
            next_end1 = start1 + (i + 1) * ran
            next_start2 = start2 + j * ran
            next_end2 = start2 + (j + 1) * ran
            paper_cnt(next_start1, next_end1, next_start2, next_end2)

paper_cnt(0, N, 0, N)
print(*cnt, sep = "\n")