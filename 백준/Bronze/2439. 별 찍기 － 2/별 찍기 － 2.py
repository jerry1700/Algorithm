import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    # return [" " * (N - i) + "*" * i for i in range(1, N + 1)]
    return [("*" * i).rjust(N) for i in range(1, N + 1)]

def main():
    N = int(input())

    answer = solve(N)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()