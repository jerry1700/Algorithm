N = int(input())
answer = 0
isused1 = [False] * N
isused2 = [False] * (2 * N - 1)
isused3 = [False] * (2 * N - 1)

def backtrack(depth):
    global answer

    if depth == N:
        answer += 1
        return
    
    for i in range(N):
        first = depth + i
        second = depth - i + N - 1
        if isused1[i] or isused2[first] or isused3[second]:
            continue
        isused1[i] = True
        isused2[first] = True
        isused3[second] = True
        backtrack(depth + 1)
        isused1[i] = False
        isused2[first] = False
        isused3[second] = False

backtrack(0)
print(answer)