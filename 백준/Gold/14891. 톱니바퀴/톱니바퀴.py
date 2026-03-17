from collections import deque

wheels = [deque(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    dic = [0] * 4
    visited = [False] * 4

    start = n - 1
    deq = deque([(start, d)])
    while deq:
        num, dir = deq.popleft()
        visited[num] = True
        dic[num] = dir

        if num - 1 >= 0 and not visited[num - 1] and wheels[num - 1][2] != wheels[num][6]:
            deq.append((num - 1, -dir))
        if num + 1 < 4 and not visited[num + 1] and wheels[num][2] != wheels[num + 1][6]:
            deq.append((num + 1, -dir))

        wheels[num].rotate(dir)

answer = 0
for i in range(4):
    if wheels[i][0] == 1:
        answer += (2 ** i)
print(answer)