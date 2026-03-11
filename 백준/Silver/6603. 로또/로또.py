def backtracking(start, depth, k, S, sequence):
    if depth == 6:
        print(" ".join(map(str, sequence)))
        return
    for i in range(start, k):
        sequence.append(S[i])
        backtracking(i + 1, depth + 1, k, S, sequence)
        sequence.pop()

while True:
    temp = list(map(int, input().split()))
    if temp == [0]:
        break
    k = temp[0]
    S = temp[1:]

    sequence = []
    backtracking(0, 0, k, S, sequence)
    print()