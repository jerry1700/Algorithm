from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < x < x2 * 2 and y1 * 2 < y < y2 * 2:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1 
            
    dist = [[0] * 102 for _ in range(102)]
    dist[characterX * 2][characterY * 2] = 0
    q = deque([(characterX * 2, characterY * 2)])
    
    while q:
        x, y = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            return dist[x][y] // 2
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and board[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))