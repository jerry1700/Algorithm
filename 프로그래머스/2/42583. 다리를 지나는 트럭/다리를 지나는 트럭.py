from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    time = 0
    limit = 0
    
    while q or limit > 0:
        limit -= bridge[0]
        bridge.popleft()
        
        if q:
            if limit + q[0] <= weight:
                limit += q[0]
                bridge.append(q.popleft())
            else:
                bridge.append(0)
                
        time += 1
        
    return time 