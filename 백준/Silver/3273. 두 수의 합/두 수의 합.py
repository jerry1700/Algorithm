import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums, x):
    good = set()
    cnt = 0

    for i in nums:
        if i in good:
            cnt += 1
            good.remove(i)
        else:
            good.add(x - i)

    return cnt

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    answer = solve(nums, x)
    print(answer)

if __name__ == "__main__":
    main()