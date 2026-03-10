N, M = map(int, input().split())
sequences = []
sequence = []

def backtracking(start, depth):
    if depth == M:
        sequences.append(" ".join(map(str, sequence)))
        return
    for i in range(start, N + 1):
        sequence.append(i)
        backtracking(start, depth + 1)
        sequence.pop()
        start += 1

backtracking(1, 0)
print(*sequences, sep = "\n")