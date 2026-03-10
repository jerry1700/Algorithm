import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(reverse_case):
    cards = list(range(1, 21))
    for i, j in reverse_case:
        cards[i - 1:j] = cards[i - 1:j][::-1]
    return cards

def main():
    reverse_case = [(a, b) for a, b in (map(int, input().split()) for _ in range(10))]

    answer = solve(reverse_case)
    print(*answer)

if __name__ == "__main__":
    main()