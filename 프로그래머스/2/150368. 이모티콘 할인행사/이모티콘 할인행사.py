from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    cnt = len(emoticons)
    answer = [0, 0]
    
    for dis in product(discounts, repeat=cnt):
        result = [0, 0]
        emo = [(d, emoticons[idx] * (100 - d) / 100) for idx, d in enumerate(dis)]
        
        for x, y in users:
            num = 0
            for xx, yy in emo:
                if xx >= x:
                    num += yy
            
            if num >= y:
                result[0] += 1
            else:
                result[1] += num
                
        if result[0] > answer[0]:
            answer = result
        elif result[0] == answer[0] and result[1] > answer[1]:
                answer[1] = result[1]
    
    return answer