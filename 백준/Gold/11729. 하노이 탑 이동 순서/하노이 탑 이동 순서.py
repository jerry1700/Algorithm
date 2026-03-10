N = int(input())

def hanoi(a, b, N):
    if N == 1:
        print(a, b)
    else:
        hanoi(a, 6 - a - b, N - 1)
        print(a, b)
        return hanoi(6 - a - b, b, N - 1)

print(2 ** N - 1)
hanoi(1, 3, N)