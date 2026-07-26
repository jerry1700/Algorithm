def solution(s):
    ops = list(s.split())
    answer = 0
    for i, op in enumerate(ops):
        if op == "Z":
            answer -= int(ops[i - 1])
        else:
            answer += int(op)
        
    return answer