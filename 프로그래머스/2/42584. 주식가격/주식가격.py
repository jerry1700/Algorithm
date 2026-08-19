def solution(prices):
    answer = []
    
    for i, p in enumerate(prices):
        num = 0
        for j in range(i + 1, len(prices)):
            num += 1
            if p > prices[j]:
                break
        
        answer.append(num)
        
    return answer