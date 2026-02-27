import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N, K):
    num = list(range(1, N + 1))
    stack = []
    start = K - 1
    step = K - 1

    for i in range(N):
        if start < len(num):
            stack.append(num[start])
            num.pop(start)
            start += step
        else:
            while start >= len(num):
                start -= len(num)
            stack.append(num[start])
            num.pop(start)
            start += step

    return f"<{', '.join(map(str, stack))}>"

def main():
    N, K = map(int, input().split())

    answer = solve(N, K)
    print(answer)

if __name__ == "__main__":
    main()