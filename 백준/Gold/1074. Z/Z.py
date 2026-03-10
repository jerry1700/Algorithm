N, r, c = map(int, input().split())

def square(N, r, c):
    half = 2 ** (N - 1)
    if N == 0:
        return 0
    if 0 <= r < half and 0 <= c < half:
        return square(N - 1, r, c)
    elif 0 <= r < half and half <= c < 2 ** N:
        return half ** 2 + square(N - 1, r, c - half)
    elif half <= r < 2 ** N and 0 <= c < half:
        return 2 * half ** 2 + square(N - 1, r - half, c)
    elif half <= r < 2 ** N and half <= c < 2 ** N:
        return 3 * half ** 2 + square(N - 1, r - half, c - half)

print(square(N, r, c))