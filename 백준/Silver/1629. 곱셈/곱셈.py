A, B, C = map(int, input().split())

def mod(A, B, C):
    if B == 0:
        return 1
    result = mod(A, B // 2, C)
    result = (result * result) % C
    if B % 2 == 0:
        return result
    return (result * A) % C

answer = mod(A, B, C)
print(answer)