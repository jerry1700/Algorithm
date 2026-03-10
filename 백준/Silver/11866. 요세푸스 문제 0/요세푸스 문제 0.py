N, K = map(int, input().split())
num = list(range(1, N + 1))

stack = []
start = K - 1
step = K - 1
for i in range(N):
    if start < len(num):
        stack.append(num[start])
        num.pop(start)
        start += step
    else:
        while start >= len(num):
            start -= len(num)
        stack.append(num[start])
        num.pop(start)
        start += step

print(f"<{', '.join(map(str, stack))}>")
