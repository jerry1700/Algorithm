import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    up = [" " * (N - i) + "*" * (2 * i - 1) for i in range(1, N + 1)]
    down = [" " * (N - i) + "*" * (2 * i - 1) for i in range(N - 1, 0, -1)]
    return up + down

def main():
    N = int(input())

    answer = solve(N)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()