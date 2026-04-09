import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip()

N, C = map(int, input().split())
nums = list(map(int, input().split()))

nums = Counter(nums)

for item, count in nums.most_common():
    for _ in range(count):
        print(item, end = " ")