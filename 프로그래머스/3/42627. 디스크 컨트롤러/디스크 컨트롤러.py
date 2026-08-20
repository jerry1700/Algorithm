def solution(jobs):
    jobs = [[job[0], job[1], idx] for idx, job in enumerate(jobs)]
    time = 0
    answer = []
        
    while jobs:
        if time == 0:
            jobs = sorted(jobs)
            i, j, k = jobs.pop(0)
            
            time += i
            time += j
            answer.append(time - i)
        else:
            jobs = sorted(jobs, key=lambda x: (0 if x[0] <= time else 1, x[1]))
            i, j, k = jobs.pop(0)

            if time <= i:
                time = i
            time += j
            answer.append(time - i)

    return int(sum(answer) / len(answer))