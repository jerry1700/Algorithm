def solution(spell, dic):
    answer = 2
    for word in dic:
        test = False
        for s in spell:
            if s not in word:
                break
            
            if s == spell[-1]:
                test = True
                
        if test:
            answer = 1
                
    return answer