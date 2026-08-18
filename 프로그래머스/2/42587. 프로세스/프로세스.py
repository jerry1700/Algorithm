from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    num = [i for i in range(1, len(priorities) + 1)]
    num = deque(num)
    end = num[location]
    
    answer = 0
    while q:
        if q[0] == max(q):
            if num[0] == end:
                return answer + 1
            
            q.popleft()
            num.popleft()
            answer += 1
        else:
            q.rotate(-1)
            num.rotate(-1)