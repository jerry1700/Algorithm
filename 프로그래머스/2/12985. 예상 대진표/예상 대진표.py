def solution(n,a,b):
    if a < b:
        num = 1
        while a % 2 != 1 or b % 2 != 0 or a + 1 != b:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a // 2 + 1
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 + 1
            
            num += 1
            
        answer = num
        
    else:
        num = 1
        while not (a % 2 == 0 and b % 2 == 1) or a != b + 1:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a // 2 + 1
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 + 1
            
            num += 1
            
        answer = num

    return answer