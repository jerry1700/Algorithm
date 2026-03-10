N = int(input())
answer = [[" " for _ in range(N)] for _ in range(N)]

def star(N, x, y):
    if N == 1:
        answer[x][y] = "*"
        return
    
    step = N // 3
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            star(step, x + i * step, y + j * step)
                
star(N, 0, 0)
for a in answer:
    print("".join(a))