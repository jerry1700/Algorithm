N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1
    ladder[a - 1][b] = -1

def check(ladder):
    for i in range(N):
        idx = i
        for j in range(H):
            idx += ladder[j][idx]
        
        if i != idx:
            return False
        
    return True

def backtracking(depth, end, start):
    global found
    
    if found:
        return
    
    if depth == end:
        if check(ladder):
            found = True
        return
    
    for xy in range(start, (N - 1) * H):
        x, y = divmod(xy, N - 1)
        if ladder[x][y] or ladder[x][y + 1]:
            continue

        ladder[x][y] = 1
        ladder[x][y + 1] = -1
        backtracking(depth + 1, end, xy + 1)
        ladder[x][y] = 0
        ladder[x][y + 1] = 0

found = False
for end in range(4):
    backtracking(0, end, 0)
    if found:
        print(end)
        exit()
print(-1)