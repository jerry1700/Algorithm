N, M, H = map(int, input().split())
ladder = [[False] * (N - 1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = True

def check(ladder):
    for i in range(N):
        idx = i
        for j in range(H):
            if idx == 0:
                if ladder[j][idx]:
                    idx += 1
            elif idx == N - 1:
                if ladder[j][idx - 1]:
                    idx -= 1
            else:
                if ladder[j][idx - 1]:
                    idx -= 1
                elif ladder[j][idx]:
                    idx += 1
        
        if i != idx:
            return False
        
    return True

def backtracking(depth, end, start):
    if depth == end:
        return check(ladder)
    
    if N == 2:
        for i in range(start, H):
            if not ladder[i][0]:
                ladder[i][0] = True
                if backtracking(depth + 1, end, i + 1):
                    return True
                ladder[i][0] = False
        return False
    else:
        for idx in range(start, H * (N - 1)):
            i = idx // (N - 1)
            j = idx % (N - 1)
            if j == 0:
                if not ladder[i][j] and not ladder[i][j + 1]:
                    ladder[i][j] = True
                    if backtracking(depth + 1, end, idx + 1):
                        return True
                    ladder[i][j] = False
            elif j == N - 2:
                if not ladder[i][j - 1] and not ladder[i][j]:
                    ladder[i][j] = True
                    if backtracking(depth + 1, end, idx + 1):
                        return True
                    ladder[i][j] = False
            else:
                if not ladder[i][j - 1] and not ladder[i][j] and not ladder[i][j + 1]:
                    ladder[i][j] = True
                    if backtracking(depth + 1, end, idx + 1):
                        return True
                    ladder[i][j] = False
        return False
    
for end in range(4):
    if backtracking(0, end, 0):
        print(end)
        exit()
print(-1)