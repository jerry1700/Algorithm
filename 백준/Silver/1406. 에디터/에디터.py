import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(text, M):
    # cursor = len(text)
    #
    # for i in order:
    #     if i[0] == "L":
    #         if cursor == 0:
    #             pass
    #         else:
    #             cursor -= 1
    #     elif i[0] == "D":
    #         if cursor == len(text):
    #             pass
    #         else:
    #             cursor += 1
    #     elif i[0] == "B":
    #         if cursor == 0:
    #             pass
    #         else:
    #             text = text[:cursor - 1] + text[cursor:]
    #             cursor -= 1
    #     else:
    #         text = text[:cursor] + [i[1]] + text[cursor:]
    #         cursor += 1
    # return text
    left_stack = list(text)
    right_stack = []

    for _ in range(M):
        order = input().split()
        op = order[0]

        if op == "L":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif op == "D":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif op == "B":
            if left_stack:
                left_stack.pop()
        elif op == "P":
            left_stack.append(order[1])

    return "".join(left_stack + list(reversed(right_stack)))

def main():
    text = list(input())
    M = int(input())
    # order = [input().split() for i in range(M)]

    answer = solve(text, M)
    # print(*answer, sep = "")
    print(answer)

if __name__ == "__main__":
    main()