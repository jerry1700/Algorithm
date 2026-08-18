def solution(s):
    group = []
    for i in s:
        if i == "(":
            group.append(1)
        else:
            if not group:
                return False
            if group[-1] == 1:
                group.pop()
            
    if not group:
        return True
    else:
        return False