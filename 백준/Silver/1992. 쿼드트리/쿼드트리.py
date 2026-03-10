N = int(input())
medias = [list(map(int, input())) for _ in range(N)]
answer = []

def quad_tree(x, y, ran, medias):
    half = ran // 2
    start = medias[x][y]
    test = True
    for i in range(ran):
        for j in range(ran):
            if medias[i + x][j + y] != start:
                test = False
                break
        
        if not test:
            break
    
    if test:
        answer.append(start)
        return
    else:
        answer.append("(")
        quad_tree(x, y, half, medias)
        quad_tree(x, y + half, half, medias)
        quad_tree(x + half, y, half, medias)
        quad_tree(x + half, y + half, half, medias)
        answer.append(")")

quad_tree(0, 0, N, medias)
print("".join(map(str, answer)))