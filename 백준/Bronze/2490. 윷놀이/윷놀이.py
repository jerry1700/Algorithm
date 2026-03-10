import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(game):
    # result = []
    #
    # for i in game:
    #     if i.count(0) == 0:
    #         result.append("E")
    #     elif i.count(0) == 1:
    #         result.append("A")
    #     elif i.count(0) == 2:
    #         result.append("B")
    #     elif i.count(0) == 3:
    #         result.append("C")
    #     else:
    #         result.append("D")
    # return result
    return ["DCBAE"[sum(i)] for i in game]

def main():
    game = [list(map(int, input().split())) for i in range(3)]

    answer = solve(game)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()