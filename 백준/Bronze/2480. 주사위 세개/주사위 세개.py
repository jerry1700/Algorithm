import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(first, second, third):
    if first == second == third:
        return 10000 + first * 1000
    elif first == second:
        return 1000 + first * 100
    elif first == third:
        return 1000 + first * 100
    elif second == third:
        return 1000 + second * 100
    else:
        return max(first, second, third) * 100

def main():
    first, second, third = map(int, input().split())

    answer = solve(first, second, third)
    print(answer)

if __name__ == "__main__":
    main()