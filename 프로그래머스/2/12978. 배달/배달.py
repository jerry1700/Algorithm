import heapq

def solution(N, road, K):
    answer = 0
    board = [[] for _ in range(N + 1)]
    for a, b, c in road:
        board[a].append((b, c))
        board[b].append((a, c))
    dist = [float("INF")] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in board[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
                
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1
            
    return answer