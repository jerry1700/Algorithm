import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip()

def solve(students, K):
    mans = [j for i, j in students if i == "1"]
    womans = [j for i, j in students if i == "0"]

    countermans = Counter(mans)
    counterwomans = Counter(womans)

    cnt = sum((c + K - 1) // K for c in countermans.values())
    cnt += sum((c + K - 1) // K for c in counterwomans.values())

    return cnt

def main():
    N, K = map(int, input().split())
    students = [list(input().split()) for i in range(N)]

    answer = solve(students, K)
    print(answer)

if __name__ == "__main__":
    main()