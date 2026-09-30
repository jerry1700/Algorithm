def solution(id_list, report, k):
    num = len(id_list)
    score = [0] * num
    ban = [0] * num
    ban_member = [[] for _ in range(num)]
    
    for r in report:
        a, b = r.split()
        
        if b not in ban_member[id_list.index(a)]:
            ban_member[id_list.index(a)].append(b)
            
    for i in range(num):
        for m in ban_member[i]:
            ban[id_list.index(m)] += 1
        
    for i in range(num):
        for m in ban_member[i]:
            if ban[id_list.index(m)] >= k:
                score[i] += 1
    
    return score