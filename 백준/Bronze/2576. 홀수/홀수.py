import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums):
    odds = [odd for odd in nums if odd % 2 == 1]
    if not odds:
        return -1,
    return sum(odds), min(odds)

def main():
    nums = [int(input()) for i in range(7)]

    answer = solve(nums)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()