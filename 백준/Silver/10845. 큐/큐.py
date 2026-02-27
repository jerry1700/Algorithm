import sys
input = sys.stdin.readline

N = int(input())

quene = []
for i in range(N):
    order = input().rstrip()

    if order[:4] == "push":
        quene.append(order[5:])
    elif order == "pop":
        if quene:
            print(quene.pop(0))
        else:
            print(-1)
    elif order == "size":
        print(len(quene))
    elif order == "empty":
        if quene:
            print(0)
        else:
            print(1)
    elif order == "front":
        if quene:
            print(quene[0])
        else:
            print(-1)
    else:
        if quene:
            print(quene[-1])
        else:
            print(-1)
