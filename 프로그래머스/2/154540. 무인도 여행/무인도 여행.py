from collections import deque

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(maps):
    width = len(maps[0])
    length = len(maps)
    
    answer = []
    visited = [[False] * width for _ in range(length)]
    for i in range(length):
        for j in range(width):
            if maps[i][j] != "X" and not visited[i][j]:
                size = int(maps[i][j])
                visited[i][j] = True
                q = deque([(i, j)])
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < length and 0 <= ny < width and not visited[nx][ny] and maps[nx][ny] != "X":
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            size += int(maps[nx][ny])
                            
                answer.append(size)
                
    answer.sort()
    if not answer:
        answer = [-1]
    
    return answer