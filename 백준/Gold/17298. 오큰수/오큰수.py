import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N, nums):
    stack = []
    large = [-1] * N

    for i in range(N):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            large[index] = nums[i]

        stack.append(i)

    return large

def main():
    N = int(input())
    nums = list(map(int, input().split()))

    answer = solve(N, nums)
    print(*answer)

if __name__ == "__main__":
    main()