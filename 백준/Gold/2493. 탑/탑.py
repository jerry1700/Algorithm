import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N, top):
    stack = []
    result = [0] * N

    for i in range(N - 1, -1, -1):
        while stack and top[stack[-1]] < top[i]:
            index = stack.pop()
            result[index] = i + 1

        stack.append(i)

    return result

def main():
    N = int(input())
    top = list(map(int, input().split()))

    answer = solve(N, top)
    print(*answer, end = " ")

if __name__ == "__main__":
    main()