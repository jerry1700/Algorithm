import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(text):
    asc = [0] * (ord("z") - ord("a") + 1)
    for i in text:
        asc[ord(i) - ord("a")] += 1
    return asc

def main():
    text = input()

    answer = solve(text)
    print(*answer)

if __name__ == "__main__":
    main()