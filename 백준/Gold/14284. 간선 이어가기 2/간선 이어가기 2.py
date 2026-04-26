import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())

dis = [float("inf")] * (n + 1) 
dis[s] = 0
hq = [(s, 0)]

while hq:
    cur_node, cur_dis = heapq.heappop(hq)

    if dis[cur_node] < cur_dis:
        continue
    
    for next_node, w in graph[cur_node]:
        cost = cur_dis + w

        if dis[next_node] > cost:
            dis[next_node] = cost
            heapq.heappush(hq, (next_node, cost))

print(dis[t])