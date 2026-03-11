N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

sequence = []

def backtracking(start, depth):
    if depth == M:
        print(" ".join(map(str, sequence)))
        return
    for i in range(start, len(nums)):
        sequence.append(nums[i])
        backtracking(i, depth + 1)
        sequence.pop()

backtracking(0, 0)