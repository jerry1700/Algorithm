def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split("."))
    
    for idx, privacie in enumerate(privacies):
        date, ty = privacie.split()
        yyyy, mm, dd = map(int, date.split("."))
        
        for term in terms:
            al, nu = term.split()
            
            if al == ty:
                mm += int(nu)
                dd -= 1
                
                while mm > 12:
                    mm -= 12
                    yyyy += 1
                
                if dd == 0:
                    dd = 28
                    mm -= 1
                
                break
        
        if yyyy < y:
            answer.append(idx + 1)
        elif yyyy == y and mm < m:
            answer.append(idx + 1)
        elif yyyy == y and mm == m and dd < d:
            answer.append(idx + 1)
                            
    return answer