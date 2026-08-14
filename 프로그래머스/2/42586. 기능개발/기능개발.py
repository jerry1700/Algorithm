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

    idx = 0
    while idx < cnt:
        num = 1

        for nidx in range(idx + 1, cnt):
            if days[idx] >= days[nidx]:
                num += 1
            else:
                break
                
        answer.append(num)

        idx += num
    
    return answer