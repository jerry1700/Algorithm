import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dis = [float("inf")] * (N + 1)
dis[1] = 0
hq = [(0, 1)]

while hq:
    cur_dis, cur_node = heapq.heappop(hq)

    if dis[cur_node] < cur_dis:
        continue

    for next_node, w in graph[cur_node]:
        cost = cur_dis + w

        if dis[next_node] > cost:
            dis[next_node] = cost
            heapq.heappush(hq, (cost, next_node))

print(dis[N])