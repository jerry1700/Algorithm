import sys
input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    order = input().rstrip()

    if order[:4] == "push":
        stack.append(order[5:])
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
