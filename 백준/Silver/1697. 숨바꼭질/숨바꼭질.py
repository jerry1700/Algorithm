from collections import deque

N, K = map(int, input().split())
distances = [-1] * 100001
visited = [False] * 100001
distances[N] = 0
visited[N] = True
deq = deque([N])

while not visited[K]:
    x = deq.popleft()
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i < 100001 and not visited[i]:
            distances[i] = distances[x] + 1
            visited[i] = True
            deq.append(i)

print(distances[K])