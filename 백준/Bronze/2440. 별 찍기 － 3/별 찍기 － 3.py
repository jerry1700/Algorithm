import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    return ["*" * i for i in range(N, 0, -1)]

def main():
    N = int(input())

    answer = solve(N)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()