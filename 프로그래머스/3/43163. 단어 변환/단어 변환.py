from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
        
    visited = [False] * len(words)
    q = deque([(begin, 0)])
    
    while q:
        x, cnt = q.popleft()
        
        if x == target:
            return cnt
        
        for idx, word in enumerate(words):
            if not visited[idx]:
                diff = sum(1 for a, b in zip(x, word) if a != b)
                
                if diff == 1:
                    visited[idx] = True
                    q.append((word, cnt + 1))