import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(room):
    asc = [0] * 10

    for i in room:
        asc[int(i)] += 1

    asc[6] = int((asc[6] + asc[9]) / 2 + 0.5)
    asc.pop()

    return max(asc)

def main():
    room = input()

    answer = solve(room)
    print(answer)

if __name__ == "__main__":
    main()