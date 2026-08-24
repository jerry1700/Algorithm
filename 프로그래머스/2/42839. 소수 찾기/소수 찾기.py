from itertools import permutations

def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers) + 1):
        for p in list(permutations(numbers, i)):
            p = int(''.join(p))
            
            if p == 2:
                answer.append(p)
            
            prime = True
            for i in range(2, p // 2 + 2):
                if p % i == 0:
                    prime = False
                    break
            
            if prime:
                answer.append(p)
                
    answer = set(answer)
            
    return sum(1 for a in answer if a >= 2)