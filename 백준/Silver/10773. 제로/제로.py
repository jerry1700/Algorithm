import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(K):
    money = []

    for _ in range(K):
        m = int(input())
        if m != 0:
            money.append(m)
        else:
            money.pop()

    return sum(money)

def main():
    K = int(input())

    answer = solve(K)
    print(answer)

if __name__ == "__main__":
    main()