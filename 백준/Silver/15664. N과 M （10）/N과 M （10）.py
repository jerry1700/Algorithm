N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
is_used = [False] * N

sequence = []

def backtracking(start, depth):
    if depth == M:
        print(*sequence)
        return

    last_num = 0
    for i in range(start, N):
        if not is_used[i] and nums[i] != last_num:
            is_used[i] = True
            sequence.append(nums[i])
            last_num = nums[i]
            backtracking(i, depth + 1)
            sequence.pop()
            is_used[i] = False

backtracking(0, 0)