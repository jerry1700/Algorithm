from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5

    q = deque()
    
    for city in cities:
        city = city.lower()
        
        if len(q) < cacheSize:
            if city in q:
                q.remove(city)
                answer += 1
                q.append(city)
            else:
                answer += 5
                q.append(city)
        else:
            if city in q:
                q.remove(city)
                answer += 1
                q.append(city)
            else:
                q.popleft()
                answer += 5
                q.append(city)
    
    return answer