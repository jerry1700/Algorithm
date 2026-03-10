T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    importance = list(map(str, input().split()))
    revision = list(map(int, importance))

    for i in range(len(importance)):
        importance[i] += f"{i}"

    x = importance[M]

    answer = []

    while len(revision) > 0:
        if revision[0] == max(revision):
            revision.pop(0)
            answer.append(importance[0])
            importance.pop(0)
        else:
            a = revision.pop(0)
            revision.append(a)
            a = importance.pop(0)
            importance.append(a)

    print(answer.index(x) + 1)
