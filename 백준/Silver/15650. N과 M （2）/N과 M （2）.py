N, M = map(int, input().split())
answer = []
test = []
is_used = [False] * (N + 1)

def backtrack(start, depth):
    if depth == M:
        answer.append(" ".join(map(str, test)))
        return
    for i in range(start + 1, N + 1):
        if not is_used[i]:
            is_used[i] = True
            test.append(i)
            backtrack(i, depth + 1)
            test.pop()
            is_used[i] = False

backtrack(0, 0)
print(*answer, sep = "\n")