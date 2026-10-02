def solution(s):
    num = len(s)
    answer = num
    
    for i in range(num // 2, 0, -1):
        tmp = []
        start = s[:i]
        cnt = 1
        idx = i
        
        while idx <= num:
            if start == s[idx:idx + i]:
                cnt += 1
            else:
                if cnt > 1:
                    tmp.append(str(cnt))
                    tmp.append(start)
                else:
                    tmp.append(start)
                    
                cnt = 1
                start = s[idx:idx + i]
                
            idx += i
        
        if cnt > 1:
            tmp.append(str(cnt))
            tmp.append(start)
        else:
            tmp.append(start)
        
        next = len("".join(tmp))
        if next < answer:
            answer = next
    
    return answer