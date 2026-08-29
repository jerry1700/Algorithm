from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    dist[0][0] = 1
    
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return dist[x][y]
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == 0 and maps[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return -1