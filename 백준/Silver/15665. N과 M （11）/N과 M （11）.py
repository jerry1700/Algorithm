N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

sequence = []

def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, sequence)))
        return
    for i in range(len(nums)):
        sequence.append(nums[i])
        backtracking(depth + 1)
        sequence.pop()

backtracking(0)