from itertools import combinations

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]

answer = float("inf")

for team1 in combinations(range(N), N // 2):
    team2 = [t for t in range(N) if t not in team1]
    stat1 = 0
    stat2 = 0
    for x, y in combinations(team1, 2):
        stat1 += stat[x][y] + stat[y][x]
    for x, y in combinations(team2, 2):
        stat2 += stat[x][y] + stat[y][x]
    
    diff = abs(stat1 - stat2)
    if diff < answer:
        answer = diff

    if answer == 0:
        break
    
print(answer)