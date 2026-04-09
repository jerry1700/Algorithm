import sys

def input():
    return sys.stdin.readline().rstrip()

tmp = input().split()
n = int(tmp[0])
nums = tmp[1:]
while True:
    if len(nums) == n:
        break

    tmp = input().split()
    nums += tmp

for idx, i in enumerate(nums):
    nums[idx] = int(i[::-1])

print(*sorted(nums), sep = "\n")