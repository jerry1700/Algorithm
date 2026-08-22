def solution(sizes):
    x = [min(s) for s in sizes]
    y = [max(s) for s in sizes]
    
    return max(x) * max(y)