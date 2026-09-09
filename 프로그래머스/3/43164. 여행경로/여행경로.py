from collections import deque

def solution(tickets):
    num = len(tickets)
    routes = []
    
    q = deque()
    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            q.append((["ICN", ticket[1]], [i]))
            
    while q:
        path, visited_idx = q.popleft()
        
        if len(path) == num + 1:
            routes.append(path)
            continue
            
        for i in range(num):
            if i not in visited_idx and tickets[i][0] == path[-1]:
                q.append((path + [tickets[i][1]], visited_idx + [i]))

    routes.sort()
    return routes[0]