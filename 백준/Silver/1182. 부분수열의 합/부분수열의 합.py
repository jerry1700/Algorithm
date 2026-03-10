N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def backtracking(idx, total):
    global cnt
    if idx == N:
        if total == S:
            cnt += 1
        return
    
    backtracking(idx + 1, total)
    backtracking(idx + 1, total + nums[idx])
    
backtracking(0, 0)
if S == 0:
    cnt -= 1

print(cnt)