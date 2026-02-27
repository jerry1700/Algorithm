import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums, v):
    return nums.count(v)

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    v = int(input())

    answer = solve(nums, v)
    print(answer)

if __name__ == "__main__":
    main()