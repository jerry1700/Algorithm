import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(teles):
    bill1 = 0
    bill2 = 0
    for i in teles:
        bill1 += (i // 30 + 1) * 10
        bill2 += (i // 60 + 1) * 15

    if bill1 < bill2:
        return f"Y {bill1}"
    elif bill1 > bill2:
        return f"M {bill2}"
    else:
        return f"Y M {bill1}"

def main():
    N = int(input())
    teles = list(map(int, input().split()))

    answer = solve(teles)
    print(answer)

if __name__ == "__main__":
    main()