import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(a, b):
    start, end = min(a, b), max(a, b)
    between = list(range(start + 1, end))
    return len(between), between

def main():
    a, b = map(int, input().split())

    answer = solve(a, b)
    print(answer[0])
    print(*answer[1])

if __name__ == "__main__":
    main()