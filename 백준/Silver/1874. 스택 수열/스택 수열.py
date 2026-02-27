import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(nums):
    stack = []
    answer = []
    start = 1

    for t in nums:
        while start <= t:
            stack.append(start)
            answer.append("+")
            start += 1

        if not (stack and stack[-1] == t):
            return "NO"
        
        stack.pop()
        answer.append("-")

    return "\n".join(answer)

def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    answer = solve(nums)
    print(answer)

if __name__ == "__main__":
    main()