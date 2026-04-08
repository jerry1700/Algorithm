from collections import Counter

N = int(input())
nums = [int(input()) for _ in range(N)]

count = Counter(nums)
result = sorted(count.items(), key = lambda x: (-x[1], x[0]))

print(result[0][0])