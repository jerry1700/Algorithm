import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = [0] * 10001
for _ in range(N):
    nums[int(input())] += 1

for i in range(10001):
    if nums[i] > 0:
        for _ in range(nums[i]):
            print(i)