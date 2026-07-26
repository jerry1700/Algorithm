def solution(wallpaper):
    h = len(wallpaper)
    l = len(wallpaper[0])
    answer = []
    
    candi = []
    for i in range(h):
        for j in range(l):
            if wallpaper[i][j] == "#":
                candi.append(i)
                
    candi.sort()
    answer.append(candi[0])
    answer.append(candi[-1] + 1)
    
    candi = []
    for i in range(h):
        for j in range(l):
            if wallpaper[i][j] == "#":
                candi.append(j)
                
    candi.sort()
    answer.insert(1, candi[0])
    answer.append(candi[-1] + 1)
    
    return answer