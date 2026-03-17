from collections import deque

wheel1 = deque(list(map(int, input())))
wheel2 = deque(list(map(int, input())))
wheel3 = deque(list(map(int, input())))
wheel4 = deque(list(map(int, input())))
group = [wheel1, wheel2, wheel3, wheel4]
K = int(input())

answer = 0
for _ in range(K):
    dic = [0] * 4
    n, d = map(int, input().split())
    dic[n - 1] = d

    if n == 1:
        for i in range(3):
            if group[n - 1 + i][2] != group[n + i][6]:
                if dic[n - 1 + i] == 1:
                    dic[n + i] = -1
                elif dic[n - 1 + i] == -1:
                    dic[n + i] = 1
    elif n == 2:
        if group[0][2] != group[1][6]:
            if dic[1] == 1:
                dic[0] = -1
            elif dic[1] == -1:
                dic[0] = 1
        if group[1][2] != group[2][6]:
            if dic[1] == 1:
                dic[2] = -1
            elif dic[1] == -1:
                dic[2] = 1
        if group[2][2] != group[3][6]:
            if dic[2] == 1:
                dic[3] = -1
            elif dic[2] == -1:
                dic[3] = 1
    elif n == 3:
        if group[1][2] != group[2][6]:
            if dic[2] == 1:
                dic[1] = -1
            elif dic[2] == -1:
                dic[1] = 1
        if group[2][2] != group[3][6]:
            if dic[2] == 1:
                dic[3] = -1
            elif dic[2] == -1:
                dic[3] = 1
        if group[0][2] != group[1][6]:
            if dic[1] == 1:
                dic[0] = -1
            elif dic[1] == -1:
                dic[0] = 1
    elif n == 4:
        for i in range(3):
            if group[n - 1 - i][6] != group[n - 2 - i][2]:
                if dic[n - 1 - i] == 1:
                    dic[n - 2 - i] = -1
                elif dic[n - 1 - i] == -1:
                    dic[n - 2 - i] = 1

    for idx, i in enumerate(dic):
        if i == 1:
            group[idx].rotate(1)
        elif i == -1:
            group[idx].rotate(-1)

for i in range(4):
    if group[i][0] == 1:
        answer += (2 ** i)

print(answer)