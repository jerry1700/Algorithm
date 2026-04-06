import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = [int(input()) for _ in range(N)]

print(*reversed(sorted(nums)), sep = "\n")