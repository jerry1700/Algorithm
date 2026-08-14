def solution(progresses, speeds):
    answer = []
    days = []
    cnt = len(progresses)
    
    for i in range(cnt):
        re = 100 - progresses[i]
        if re % speeds[i] == 0:
            days.append(re // speeds[i])
        else:
            days.append(re // speeds[i] + 1)

    next = 0
    for i in range(cnt):
        if i < next:
            continue
        
        num = 1
        for j in range(i + 1, cnt):
            if days[i] >= days[j]:
                num += 1
            else:
                break
        
        answer.append(num)
        next += num
    
    return answer