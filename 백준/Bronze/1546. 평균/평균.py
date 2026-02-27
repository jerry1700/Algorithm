N = int(input())
scores = list(map(int, input().split()))
scores_max = max(scores)

new_scores = []
for i in scores:
    new_scores.append(i / scores_max * 100)

print(sum(new_scores) / N)
