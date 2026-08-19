def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for i in range(citations[0], -1, -1):
        x, y = 0, 0
        for c in citations:
            if c >= i:
                x += 1
            else:
                y += 1
                
        if x >= i and y <= i:
            return i