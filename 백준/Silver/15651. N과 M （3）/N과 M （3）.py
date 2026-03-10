N, M = map(int, input().split())
answer = []
sequence = []

def backtracking(depth):
    if depth == M:
        answer.append(" ".join(map(str, sequence)))
        return
    for i in range(1, N + 1):
        sequence.append(i)
        backtracking(depth + 1)
        sequence.pop()

backtracking(0)
print(*answer, sep = "\n")