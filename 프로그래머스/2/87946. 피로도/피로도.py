from itertools import permutations

def solution(k, dungeons):
    can = [i for i in range(len(dungeons))]
    can = list(permutations(can, len(dungeons)))
    
    answer = 0
    for p in can:
        result = 0
        temp = k
        
        for i in p:
            x, y = dungeons[i]
            
            if k >= x:
                k -= y
                result += 1
        
        if result > answer:
            answer = result
            
        k = temp
        if result == len(dungeons):
            return result
        
    return answer