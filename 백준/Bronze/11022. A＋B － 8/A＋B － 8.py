T = int(input())
for i in range(T):
    a, b = map(int, list(input().split(" ")))
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')
    