import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums):
    nums = sorted(nums)
    return nums[0], nums[1], nums[2]

def main():
    nums = list(map(int, input().split()))

    answer = solve(nums)
    print(*answer, end = " ")

if __name__ == "__main__":
    main()