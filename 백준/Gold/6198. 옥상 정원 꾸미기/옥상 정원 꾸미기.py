import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N, buildings):
    stack = []
    cnt = 0

    for i in range(N):
        while stack and buildings[stack[-1]] <= buildings[i]:
            index = stack.pop()
            cnt += i - index - 1

        stack.append(i)

    for i in stack:
        cnt += N - i - 1
    
    return cnt

def main():
    N = int(input())
    buildings = [int(input()) for _ in range(N)]

    answer = solve(N, buildings)
    print(answer)

if __name__ == "__main__":
    main()