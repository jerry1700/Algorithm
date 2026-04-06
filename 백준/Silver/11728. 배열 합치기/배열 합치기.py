N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

i, j = 0, 0
result = []

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1
result.extend(A[i:])
result.extend(B[j:])

print(*result)