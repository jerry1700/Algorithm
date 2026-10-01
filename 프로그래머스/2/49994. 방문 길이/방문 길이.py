def solution(dirs):
    answer = []
    x, y = 5, 5
    
    for dir in dirs:
        if dir == "U":
            if x + 1 < 11:
                answer.append([(x, y), (x + 1, y)])
                x += 1
        elif dir == "D":
            if x - 1 >= 0:
                answer.append([(x - 1, y), (x, y)])
                x -= 1
        elif dir == "R":
            if y + 1 < 11:
                answer.append([(x, y), (x, y + 1)])
                y += 1
        elif dir == "L":
            if y - 1 >= 0:
                answer.append([(x, y - 1), (x, y)])
                y -= 1
            
    answer = sorted(answer)
    result = [answer[0]]
    
    for idx, a in enumerate(answer):
        if idx == 0:
            continue
        
        if result[-1] != a:
            result.append(a)
    
    return len(result)