import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(case):
    result = []

    for i, j in case:
        asc1 = [0] * (ord("z") - ord("a") + 1)
        for a in i:
            asc1[ord(a) - ord("a")] += 1

        asc2 = [0] * (ord("z") - ord("a") + 1)
        for b in j:
            asc2[ord(b) - ord("a")] += 1

        if asc1 == asc2:
            result.append("Possible")
        else:
            result.append("Impossible")

    return result

def main():
    N = int(input())
    case = [input().split() for i in range(N)]

    answer = solve(case)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()