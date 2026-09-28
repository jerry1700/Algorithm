from itertools import combinations_with_replacement

def solution(n, info):
    scores = list(range(11))
    num = 0
    answer = [-1]
    
    for score in combinations_with_replacement(scores, n):
        result = [0] * 11
        apeach, lion = 0, 0
        
        for s in score:
            result[s] += 1
            
        for x in range(11):
            if result[x] > 0 or info[x] > 0:
                if result[x] > info[x]:
                    lion += 10 - x
                else:
                    apeach += 10 - x
                
        if lion - apeach > num:
            num = lion - apeach
            answer = result
        elif lion - apeach == num:
            for x in range(10, -1, -1):
                if len(answer) > 1:
                    if result[x] != answer[x]:
                        if result[x] > answer[x]:
                            answer = result
                        break
    
    return answer