N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
sequences = []
sequence = []
is_used = [False] * N

def backtracking(depth):
    if depth == M:
        sequences.append(" ".join(map(str, sequence)))
        return
    for i in range(N):
        if not is_used[i]:
            is_used[i] = True
            sequence.append(nums[i])
            backtracking(depth + 1)
            is_used[i] = False
            sequence.pop()

backtracking(0)
print(*sequences, sep = "\n")