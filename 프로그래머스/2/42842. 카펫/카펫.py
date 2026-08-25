def solution(brown, yellow):
    cg = []
    for i in range(yellow, 0, -1):
        if yellow % i == 0:
            cg.append((i, yellow // i))
    
    can = (brown - 4) // 2
    for x, y in cg:
        if x + y == can:
            return [x + 2, y + 2]