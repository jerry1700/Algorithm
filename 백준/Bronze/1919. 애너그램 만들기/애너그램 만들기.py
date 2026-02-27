import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(first, second):
    first_alpha = [0] * (ord("z") - ord("a") + 1)
    second_alpha = [0] * (ord("z") - ord("a") + 1)

    for i in first:
        first_alpha[ord(i) - ord("a")] += 1
    for j in second:
        second_alpha[ord(j) - ord("a")] += 1

    return sum([abs(first_alpha[c] - second_alpha[c]) for c in range(len(first_alpha))])

def main():
    first = input()
    second = input()

    answer = solve(first, second)
    print(answer)

if __name__ == "__main__":
    main()