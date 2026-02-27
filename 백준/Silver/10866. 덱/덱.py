import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def solve(N):
    que = deque()
    output = []

    for _ in range(N):
        order = input().split()
        op = order[0]

        if op == "push_front":
            que.appendleft(order[1])
        elif op == "push_back":
            que.append(order[1])
        elif op == "pop_front":
            output.append(que.popleft() if que else -1)
        elif op == "pop_back":
            output.append(que.pop() if que else -1)
        elif op == "size":
            output.append(len(que))
        elif op == "empty":
            output.append(0 if que else 1)
        elif op == "front":
            output.append(que[0] if que else -1)
        else:
            output.append(que[-1] if que else -1)

    return output


def main():
    N = int(input())
    
    answer = solve(N)
    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()