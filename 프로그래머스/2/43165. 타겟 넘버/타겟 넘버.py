from itertools import product

def solution(numbers, target):
    answer = 0
    sign = [0, 1]
    cnt = len(numbers)
    result = list(product(sign, repeat=cnt))
    
    for r in result:
        num = 0
        for i in range(cnt):
            if r[i] == 0:
                num += numbers[i]
            else:
                num -= numbers[i]
                
        if num == target:
            answer += 1
    
    return answer