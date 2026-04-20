N = int(input())
scores = [input().split() for _ in range(N)]

scores = sorted(scores, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(scores[i][0])