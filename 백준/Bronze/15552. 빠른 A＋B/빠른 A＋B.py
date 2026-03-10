import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(AB):
    sum = [a + b for a, b in AB]
    return sum

def main():
    T = int(input())
    AB = [(a, b) for a, b in (map(int, input().split()) for _ in range(T))]

    answer = solve(AB)
    sys.stdout.write("\n".join(map(str, answer)))

if __name__ == "__main__":
    main()