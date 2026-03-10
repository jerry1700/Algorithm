import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums):
    return sum(nums) // 5, sorted(nums)[2]

def main():
    nums = [int(input()) for i in range(5)]

    answer = solve(nums)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()