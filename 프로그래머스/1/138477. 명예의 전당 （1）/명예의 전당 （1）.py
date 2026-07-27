def solution(k, score):
    answer = []
    top = []
    for i in score:
        top.append(i)
        top.sort()
        top.reverse()
        
        if len(top) > k:  
            top.pop()

        answer.append(top[-1])
        
    return answer