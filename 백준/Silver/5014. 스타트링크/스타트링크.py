from collections import deque

F, S, G, U, D = map(int, input().split())

stairs = [-1] * (F + 1)
stairs[S] = 0
deq = deque([S])

visited = [False] * (F + 1)
visited[S] = True

answer = "use the stairs"
while deq:
    x = deq.popleft()
    if x == G:
        answer = stairs[x]
        break
    for nx in [x + U, x - D]:
        if 1 <= nx <= F and not visited[nx]:
            visited[nx] = True
            stairs[nx] = stairs[x] + 1
            deq.append(nx)

print(answer)