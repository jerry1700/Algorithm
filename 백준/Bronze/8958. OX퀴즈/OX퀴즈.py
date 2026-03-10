T = int(input())

for test in range(T):
    answer = input()

    score = 0
    score_sum = 0

    for i in answer:
        if i == "O":
            score += 1
            score_sum += score
        else:
            score = 0

    print(score_sum)
