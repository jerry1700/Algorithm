N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

def backtracking(start, depth):
    global result

    if depth == M:
        answer = 0
        for i, j in homes:
            distance = N * N
            for c in sequence:
                x, y = chickens[c]
                if abs(i - x) + abs(j - y) < distance:
                    distance = abs(i - x) + abs(j - y)
            answer += distance

        if answer < result:
            result = answer
        return
    
    for i in range(start, len(chickens)):
        sequence.append(i)
        backtracking(i + 1, depth + 1)
        sequence.pop()

sequences = []
sequence = []
result = float('inf')
backtracking(0, 0)

print(result)