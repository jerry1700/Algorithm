import sys

def input():
    return sys.stdin.readline().rstrip()

tmp = input().split()
n, nums = int(tmp[0]), tmp[1:]
while len(nums) < n:
    nums.extend(input().split())

for idx, num in enumerate(nums):
    nums[idx] = int(num[::-1])

print(*sorted(nums), sep = "\n")