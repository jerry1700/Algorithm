N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sequences = []
sequence = []

def backtracking(start, depth):
    if depth == M:
        sequences.append(" ".join(map(str, sequence)))
        return
    for i in range(start, N):
        sequence.append(nums[i])
        backtracking(i, depth + 1)
        sequence.pop()

backtracking(0, 0)
print(*sequences, sep = "\n")